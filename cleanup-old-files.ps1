# 清理旧 HTML 文件的脚本
# 此脚本将把所有旧的 HTML 文件移动到备份目录

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  清理旧 HTML 文件" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 创建备份目录
$backupDir = "html-backup"
if (-not (Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
    Write-Host "✓ 创建备份目录: $backupDir" -ForegroundColor Green
} else {
    Write-Host "✓ 备份目录已存在: $backupDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "移动旧 HTML 文件到备份目录..." -ForegroundColor Yellow
Write-Host ""

# 要移动的 HTML 文件列表（排除 index.html）
$htmlFiles = @(
    "about.html",
    "byd-seagull.html",
    "byd-yuan-plus.html",
    "charging.html",
    "contact.html",
    "farizon-v6e.html",
    "home.html",
    "id4-crozz.html",
    "inventory.html",
    "kia-ev5.html",
    "leapmotor-c16.html",
    "rental.html",
    "services.html",
    "song-plus.html",
    "suv.html",
    "taxi.html",
    "testdrive.html",
    "toyota-bz3.html",
    "toyota-corolla-cross-frontlander.html",
    "toyota-corolla-cross-highland.html"
)

$movedCount = 0
$notFoundCount = 0

foreach ($file in $htmlFiles) {
    if (Test-Path $file) {
        try {
            Move-Item -Path $file -Destination $backupDir -Force
            Write-Host "  ✓ 已移动: $file" -ForegroundColor Green
            $movedCount++
        } catch {
            Write-Host "  ✗ 移动失败: $file - $_" -ForegroundColor Red
        }
    } else {
        Write-Host "  - 文件不存在: $file" -ForegroundColor Gray
        $notFoundCount++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  清理完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "统计信息：" -ForegroundColor Yellow
Write-Host "  已移动文件: $movedCount" -ForegroundColor White
Write-Host "  未找到文件: $notFoundCount" -ForegroundColor White
Write-Host ""
Write-Host "所有旧 HTML 文件已备份到: $backupDir" -ForegroundColor Green
Write-Host "index.html 保留为 Vue 项目入口文件" -ForegroundColor Cyan
Write-Host ""
Write-Host "现在可以运行: npm run dev" -ForegroundColor Yellow
Write-Host ""

