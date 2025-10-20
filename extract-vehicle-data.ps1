# 从 HTML 文件提取车辆数据的辅助脚本
# 使用方法: .\extract-vehicle-data.ps1 -HtmlFile "html-backup/byd-seagull.html"

param(
    [Parameter(Mandatory=$true)]
    [string]$HtmlFile
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  车辆数据提取工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $HtmlFile)) {
    Write-Host "错误: 文件不存在 - $HtmlFile" -ForegroundColor Red
    exit 1
}

Write-Host "正在读取文件: $HtmlFile" -ForegroundColor Yellow
Write-Host ""

$content = Get-Content $HtmlFile -Raw

# 提取车辆名称
if ($content -match '<h2>(.*?)</h2>') {
    $vehicleName = $matches[1]
    Write-Host "车辆名称:" -ForegroundColor Green
    Write-Host "  $vehicleName" -ForegroundColor White
    Write-Host ""
}

# 提取描述
if ($content -match '<div class="vehicle-description">\s*<p>(.*?)</p>') {
    $description = $matches[1]
    Write-Host "车辆描述:" -ForegroundColor Green
    Write-Host "  $description" -ForegroundColor White
    Write-Host ""
}

# 提取图片
Write-Host "图片列表:" -ForegroundColor Green
$imageMatches = [regex]::Matches($content, '<img src="([^"]+)"[^>]*alt="Vehicle Image')
if ($imageMatches.Count -gt 0) {
    foreach ($match in $imageMatches) {
        $imagePath = $match.Groups[1].Value
        # 转换路径格式
        $imagePath = $imagePath -replace '\\', '/'
        if (-not $imagePath.StartsWith('/')) {
            $imagePath = "/$imagePath"
        }
        Write-Host "  '$imagePath'," -ForegroundColor White
    }
} else {
    Write-Host "  未找到图片" -ForegroundColor Gray
}
Write-Host ""

# 提取颜色
Write-Host "颜色选项:" -ForegroundColor Green
$colorMatches = [regex]::Matches($content, 'color-circle[^>]*style="background-color:\s*([^;"]+)')
if ($colorMatches.Count -gt 0) {
    foreach ($match in $colorMatches) {
        $color = $match.Groups[1].Value.Trim()
        Write-Host "  '$color'," -ForegroundColor White
    }
} else {
    Write-Host "  未找到颜色信息" -ForegroundColor Gray
}
Write-Host ""

# 提取规格表格
Write-Host "车辆规格:" -ForegroundColor Green
$specs = @{}

# Year
if ($content -match 'YEAR</th>\s*<td>([^<]+)</td>') {
    $specs['year'] = $matches[1].Trim()
}

# Make
if ($content -match 'MAKE</th>\s*<td>([^<]+)</td>') {
    $specs['make'] = $matches[1].Trim()
}

# Model
if ($content -match 'MODEL</th>\s*<td>([^<]+)</td>') {
    $specs['model'] = $matches[1].Trim()
}

# Range
if ($content -match 'RANGE</th>\s*<td>([^<]+)</td>') {
    $range = $matches[1].Trim() -replace ' ?KM', ''
    $specs['range'] = $range
}

# Seats
if ($content -match 'SEATS</th>\s*<td>([^<]+)</td>') {
    $specs['seats'] = $matches[1].Trim()
}

# Category
if ($content -match 'CATEGORY</th>\s*<td>([^<]+)</td>') {
    $specs['category'] = $matches[1].Trim()
}

# Battery Capacity
if ($content -match 'BATTERY CAPACITY</th>\s*<td>([^<]+)</td>') {
    $specs['batteryCapacity'] = $matches[1].Trim()
}

foreach ($key in $specs.Keys) {
    Write-Host "  $key : $($specs[$key])" -ForegroundColor White
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "提取完成！请将以上数据填入对应的 Vue 文件" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "参考文档: VEHICLE-DATA-GUIDE.md" -ForegroundColor Yellow
Write-Host ""

