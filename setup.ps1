# Triple Goats Vue 项目设置脚本
# 此脚本将自动设置 Vue 项目环境

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Triple Goats Vue 项目初始化脚本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查 Node.js 是否安装
Write-Host "[1/5] 检查 Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "✓ Node.js 已安装: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ 未找到 Node.js，请先安装 Node.js (https://nodejs.org/)" -ForegroundColor Red
    exit 1
}

# 检查 npm 是否安装
Write-Host "[2/5] 检查 npm..." -ForegroundColor Yellow
try {
    $npmVersion = npm --version
    Write-Host "✓ npm 已安装: $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ 未找到 npm" -ForegroundColor Red
    exit 1
}

# 安装依赖
Write-Host "[3/5] 安装项目依赖..." -ForegroundColor Yellow
Write-Host "这可能需要几分钟时间..." -ForegroundColor Gray
npm install
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ 依赖安装成功" -ForegroundColor Green
} else {
    Write-Host "✗ 依赖安装失败" -ForegroundColor Red
    exit 1
}

# 创建 public 目录
Write-Host "[4/5] 创建 public 目录..." -ForegroundColor Yellow
if (-not (Test-Path "public")) {
    New-Item -ItemType Directory -Path "public" -Force | Out-Null
    Write-Host "✓ public 目录已创建" -ForegroundColor Green
} else {
    Write-Host "✓ public 目录已存在" -ForegroundColor Green
}

# 移动静态资源
Write-Host "[5/5] 移动静态资源到 public 目录..." -ForegroundColor Yellow
$moved = 0

# 移动图片文件
$imageExtensions = @("*.jpg", "*.png", "*.svg", "*.ico", "*.webp", "*.gif")
foreach ($ext in $imageExtensions) {
    $files = Get-ChildItem -Path . -Filter $ext -File -ErrorAction SilentlyContinue
    foreach ($file in $files) {
        if ($file.Name -ne "node_modules") {
            Move-Item $file.FullName -Destination "public/" -Force -ErrorAction SilentlyContinue
            $moved++
        }
    }
}

# 移动视频文件
$videoFiles = Get-ChildItem -Path . -Include "*.mp4","*.webm" -File -ErrorAction SilentlyContinue
foreach ($file in $videoFiles) {
    Move-Item $file.FullName -Destination "public/" -Force -ErrorAction SilentlyContinue
    $moved++
}

# 移动特定文件
$specificFiles = @("site.webmanifest", "CNAME")
foreach ($fileName in $specificFiles) {
    if (Test-Path $fileName) {
        Move-Item -Path $fileName -Destination "public/" -Force -ErrorAction SilentlyContinue
        $moved++
    }
}

# 移动车辆图片文件夹
$folders = @('bz3', 'C16', 'EV5', 'frontlander', 'id4crozz', 'seagull', 'songplus', 'V6E', 'yuanplus')
foreach ($folder in $folders) {
    if (Test-Path $folder) {
        Move-Item -Path $folder -Destination "public/" -Force -ErrorAction SilentlyContinue
        $moved++
    }
}

Write-Host "✓ 已移动 $moved 个文件/文件夹到 public 目录" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  设置完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "下一步操作：" -ForegroundColor Yellow
Write-Host "1. 运行开发服务器: npm run dev" -ForegroundColor White
Write-Host "2. 在浏览器中打开: http://localhost:3000" -ForegroundColor White
Write-Host "3. 构建生产版本: npm run build" -ForegroundColor White
Write-Host ""
Write-Host "提示: 如果遇到问题，请查看 README-VUE.md 和 MIGRATION-GUIDE.md" -ForegroundColor Gray
Write-Host ""

