# 启动开发服务器的快捷脚本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  启动 Triple Goats 开发服务器" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查 node_modules 是否存在
if (-not (Test-Path "node_modules")) {
    Write-Host "未找到 node_modules 目录" -ForegroundColor Yellow
    Write-Host "正在安装依赖..." -ForegroundColor Yellow
    npm install
    Write-Host ""
}

# 启动开发服务器
Write-Host "正在启动开发服务器..." -ForegroundColor Green
Write-Host "服务器启动后将自动在浏览器中打开" -ForegroundColor Gray
Write-Host ""
Write-Host "提示: 按 Ctrl+C 停止服务器" -ForegroundColor Yellow
Write-Host ""

npm run dev

