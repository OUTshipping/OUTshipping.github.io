# 部署脚本 - 将 dist 部署到 GitHub Pages

Write-Host "开始部署到 GitHub Pages..." -ForegroundColor Green

# 构建项目
Write-Host "`n1. 构建项目..." -ForegroundColor Yellow
npm run build

if ($LASTEXITCODE -ne 0) {
    Write-Host "构建失败!" -ForegroundColor Red
    exit 1
}

# 进入 dist 目录
Write-Host "`n2. 准备部署文件..." -ForegroundColor Yellow
cd dist

# 初始化 git
git init
git add -A
git commit -m "Deploy to GitHub Pages"

# 推送到 GitHub Pages (main 分支)
Write-Host "`n3. 推送到 GitHub..." -ForegroundColor Yellow
git branch -M main
git remote add origin https://github.com/OUTshipping/OUTshipping.github.io.git

Write-Host "`n正在推送到 main 分支..." -ForegroundColor Yellow
git push -f origin main

# 返回上级目录
cd ..

Write-Host "`n部署完成! 🎉" -ForegroundColor Green
Write-Host "网站将在几分钟后在 https://tgautomobile.com 上线" -ForegroundColor Cyan

