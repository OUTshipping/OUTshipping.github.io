const sharp = require('sharp')
const fs = require('fs')
const path = require('path')

const PUBLIC_DIR = path.join(__dirname, 'public')
const MAX_WIDTH = 1920
const JPG_QUALITY = 80
const PNG_QUALITY = 80
const EXTENSIONS = ['.jpg', '.jpeg', '.png']

let totalBefore = 0
let totalAfter = 0
let processedCount = 0
let skippedCount = 0
let errorCount = 0

// 递归获取所有图片文件
function getImageFiles(dir) {
  let results = []
  const items = fs.readdirSync(dir)
  for (const item of items) {
    const fullPath = path.join(dir, item)
    const stat = fs.statSync(fullPath)
    if (stat.isDirectory()) {
      results = results.concat(getImageFiles(fullPath))
    } else if (EXTENSIONS.includes(path.extname(item).toLowerCase())) {
      results.push(fullPath)
    }
  }
  return results
}

async function compressImage(filePath) {
  const ext = path.extname(filePath).toLowerCase()
  const originalSize = fs.statSync(filePath).size
  const relativePath = path.relative(PUBLIC_DIR, filePath)

  try {
    // 用 Buffer 读取文件，绕过 sharp/libvips 对中文路径的编码问题
    const inputBuffer = fs.readFileSync(filePath)
    const image = sharp(inputBuffer)
    const metadata = await image.metadata()

    let outputBuffer
    let outputPath = filePath

    if (ext === '.png') {
      // 检查是否有透明通道
      const hasAlpha = metadata.channels === 4

      if (hasAlpha) {
        // 有透明通道：保持 PNG 格式压缩
        outputBuffer = await image
          .resize({ width: MAX_WIDTH, withoutEnlargement: true })
          .png({ quality: PNG_QUALITY, compressionLevel: 9 })
          .toBuffer()
      } else {
        // 无透明通道：转为 JPG
        const jpgPath = filePath.replace(/\.png$/i, '.jpg')
        outputBuffer = await image
          .resize({ width: MAX_WIDTH, withoutEnlargement: true })
          .jpeg({ quality: JPG_QUALITY, mozjpeg: true })
          .toBuffer()
        outputPath = jpgPath
        // 写入新 JPG 文件，删除旧 PNG
        fs.writeFileSync(outputPath, outputBuffer)
        if (outputPath !== filePath) {
          fs.unlinkSync(filePath)
        }
        const newSize = outputBuffer.length
        totalBefore += originalSize
        totalAfter += newSize
        processedCount++
        const saved = ((1 - newSize / originalSize) * 100).toFixed(1)
        console.log(`[PNG->JPG] ${relativePath} : ${formatSize(originalSize)} -> ${formatSize(newSize)} (${saved}% 减少)`)
        return
      }
    } else {
      // JPG/JPEG 压缩
      outputBuffer = await image
        .resize({ width: MAX_WIDTH, withoutEnlargement: true })
        .jpeg({ quality: JPG_QUALITY, mozjpeg: true })
        .toBuffer()
    }

    // 只有压缩后更小才覆盖
    if (outputBuffer.length < originalSize) {
      fs.writeFileSync(outputPath, outputBuffer)
      const newSize = outputBuffer.length
      totalBefore += originalSize
      totalAfter += newSize
      processedCount++
      const saved = ((1 - newSize / originalSize) * 100).toFixed(1)
      console.log(`[压缩] ${relativePath} : ${formatSize(originalSize)} -> ${formatSize(newSize)} (${saved}% 减少)`)
    } else {
      totalBefore += originalSize
      totalAfter += originalSize
      skippedCount++
      console.log(`[跳过] ${relativePath} : ${formatSize(originalSize)} (已经足够小)`)
    }
  } catch (err) {
    errorCount++
    console.error(`[错误] ${relativePath} : ${err.message}`)
  }
}

function formatSize(bytes) {
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(0) + ' KB'
  return (bytes / (1024 * 1024)).toFixed(2) + ' MB'
}

async function main() {
  console.log('开始扫描图片...\n')
  const files = getImageFiles(PUBLIC_DIR)
  console.log(`找到 ${files.length} 张图片\n`)

  for (const file of files) {
    await compressImage(file)
  }

  console.log('\n========== 压缩完成 ==========')
  console.log(`处理: ${processedCount} 张`)
  console.log(`跳过: ${skippedCount} 张`)
  console.log(`错误: ${errorCount} 张`)
  console.log(`压缩前总大小: ${formatSize(totalBefore)}`)
  console.log(`压缩后总大小: ${formatSize(totalAfter)}`)
  console.log(`总共节省: ${formatSize(totalBefore - totalAfter)} (${((1 - totalAfter / totalBefore) * 100).toFixed(1)}%)`)
}

main()

