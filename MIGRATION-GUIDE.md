# HTML 到 Vue 迁移指南

本文档详细说明如何将现有的 HTML 网站迁移到 Vue 项目。

## 📋 迁移前准备

### 1. 备份原文件
在开始迁移之前，请确保备份所有原始 HTML 文件：

```bash
# 创建备份目录
New-Item -ItemType Directory -Path html-backup -Force

# 复制所有 HTML 文件
Copy-Item -Path *.html -Destination html-backup/
```

## 🔄 迁移步骤

### 第一步：安装 Node.js
确保你的系统已安装 Node.js（版本 16 或更高）：

```bash
# 检查 Node.js 版本
node --version

# 检查 npm 版本
npm --version
```

如果未安装，请访问 https://nodejs.org/ 下载安装。

### 第二步：项目初始化

1. **安装项目依赖**
```bash
npm install
```

2. **重命名入口 HTML 文件**
```bash
# 备份原 index.html
Move-Item index.html index-old.html

# 使用 Vue 项目的 index.html
Move-Item vue-index.html index.html
```

### 第三步：组织静态资源

创建 `public` 目录并移动所有静态资源：

```powershell
# 1. 创建 public 目录
New-Item -ItemType Directory -Path public -Force

# 2. 移动图片文件
$imageFiles = Get-ChildItem -Path . -Include *.jpg,*.png,*.svg,*.ico,*.webp -File
foreach ($file in $imageFiles) {
    Move-Item $file.FullName -Destination public/ -Force
}

# 3. 移动视频文件
$videoFiles = Get-ChildItem -Path . -Include *.mp4,*.webm -File
foreach ($file in $videoFiles) {
    Move-Item $file.FullName -Destination public/ -Force
}

# 4. 移动图标和配置文件
Move-Item -Path favicon.ico,apple-touch-icon.png,site.webmanifest,favicon-96x96.png,favicon.svg,web-app-manifest-192x192.png,web-app-manifest-512x512.png -Destination public/ -ErrorAction SilentlyContinue

# 5. 移动车辆图片文件夹
$folders = @('bz3', 'C16', 'EV5', 'frontlander', 'id4crozz', 'seagull', 'songplus', 'V6E', 'yuanplus')
foreach ($folder in $folders) {
    if (Test-Path $folder) {
        Move-Item -Path $folder -Destination public/ -Force
    }
}

# 6. 移动其他可能的文件
Move-Item -Path CNAME -Destination public/ -ErrorAction SilentlyContinue
```

### 第四步：验证文件结构

确保你的项目结构如下：

```
项目根目录/
├── src/
│   ├── assets/
│   │   └── styles/
│   │       └── global.css
│   ├── components/
│   │   ├── ContactInfo.vue
│   │   ├── FooterBar.vue
│   │   ├── HeaderNav.vue
│   │   └── SocialMedia.vue
│   ├── views/
│   │   ├── vehicles/
│   │   │   ├── BYDSeagullView.vue
│   │   │   ├── BYDYuanPlusView.vue
│   │   │   ├── FarizonV6EView.vue
│   │   │   ├── ID4CrozzView.vue
│   │   │   ├── KIAEV5View.vue
│   │   │   ├── LeapmotorC16View.vue
│   │   │   ├── SongPlusView.vue
│   │   │   ├── ToyotaBZ3View.vue
│   │   │   ├── ToyotaFrontlanderView.vue
│   │   │   └── ToyotaHighlandView.vue
│   │   ├── AboutView.vue
│   │   ├── ChargingView.vue
│   │   ├── ContactView.vue
│   │   ├── HomeView.vue
│   │   ├── InventoryView.vue
│   │   ├── RentalView.vue
│   │   ├── ServicesView.vue
│   │   ├── SUVView.vue
│   │   ├── TaxiView.vue
│   │   └── TestDriveView.vue
│   ├── router/
│   │   └── index.js
│   ├── App.vue
│   └── main.js
├── public/
│   ├── bz3/
│   ├── C16/
│   ├── EV5/
│   ├── frontlander/
│   ├── id4crozz/
│   ├── seagull/
│   ├── songplus/
│   ├── V6E/
│   ├── yuanplus/
│   ├── *.jpg (所有图片)
│   ├── *.png (所有图片)
│   ├── movie.mp4
│   ├── favicon.ico
│   └── ... (其他静态资源)
├── html-backup/ (原 HTML 文件备份)
├── node_modules/
├── index.html
├── package.json
├── vite.config.js
├── .gitignore
├── README-VUE.md
└── MIGRATION-GUIDE.md (本文件)
```

### 第五步：启动开发服务器

```bash
npm run dev
```

访问 http://localhost:3000 查看网站。

## 🧪 测试迁移结果

### 1. 功能测试清单

- [ ] 首页正常显示
- [ ] 导航菜单可以正常切换
- [ ] 移动端菜单（汉堡菜单）正常工作
- [ ] 库存页面筛选功能正常
- [ ] 库存页面排序功能正常
- [ ] 社交媒体链接可以点击
- [ ] 联系表单正常显示
- [ ] Google 地图正常加载
- [ ] 所有图片正常显示
- [ ] 视频背景正常播放
- [ ] 所有内部链接正常跳转
- [ ] 响应式设计在不同设备上正常

### 2. 浏览器兼容性测试

在以下浏览器中测试：
- Chrome（推荐）
- Firefox
- Safari
- Edge

### 3. 移动端测试

使用浏览器的开发者工具测试以下设备：
- iPhone (375px)
- iPad (768px)
- 桌面 (1920px)

## 🔧 常见问题解决

### 问题 1: 图片不显示

**原因**：图片文件可能没有移动到 `public/` 目录

**解决方案**：
```bash
# 检查 public 目录
ls public/

# 手动移动缺失的图片
Move-Item missing-image.jpg public/
```

### 问题 2: 路由 404 错误

**原因**：直接访问路由地址导致 404

**解决方案**：
- 开发环境：确保使用 `npm run dev` 启动服务器
- 生产环境：配置服务器重定向所有请求到 index.html

### 问题 3: npm install 失败

**原因**：网络问题或 npm 源问题

**解决方案**：
```bash
# 使用淘宝镜像
npm config set registry https://registry.npmmirror.com

# 重新安装
npm install
```

### 问题 4: 样式显示不正确

**原因**：CSS 变量未正确加载

**解决方案**：
检查 `src/assets/styles/global.css` 是否在 `main.js` 中正确引入

## 📦 构建生产版本

### 1. 构建命令

```bash
npm run build
```

构建完成后，生产文件将在 `dist/` 目录中。

### 2. 本地预览生产构建

```bash
npm run preview
```

### 3. 部署到服务器

将 `dist/` 目录中的所有文件上传到服务器的网站根目录。

**重要**：配置服务器将所有请求重定向到 `index.html`

#### Nginx 配置示例：
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /path/to/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

#### Apache (.htaccess) 配置示例：
```apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
</IfModule>
```

## 🔄 回滚到原 HTML 版本

如果需要回滚到原始 HTML 版本：

```bash
# 1. 从备份恢复 HTML 文件
Copy-Item -Path html-backup/* -Destination . -Force

# 2. 删除或重命名 Vue 项目文件
Move-Item index.html vue-index.html -Force
Move-Item index-old.html index.html -Force

# 3. 将 public 目录中的文件移回根目录
Move-Item -Path public/* -Destination . -Force
```

## 📚 进一步学习

- [Vue 3 官方文档](https://cn.vuejs.org/)
- [Vue Router 官方文档](https://router.vuejs.org/zh/)
- [Vite 官方文档](https://cn.vitejs.dev/)

## 💡 最佳实践

1. **版本控制**：使用 Git 管理代码
2. **定期备份**：定期备份生产数据
3. **性能优化**：使用图片压缩工具优化图片大小
4. **SEO 优化**：考虑使用 SSR（服务端渲染）或预渲染
5. **错误监控**：添加错误追踪工具（如 Sentry）

## 📞 获取帮助

如果遇到问题，可以：
1. 查看 `README-VUE.md` 文档
2. 搜索 Vue.js 官方论坛
3. 联系开发团队

---

迁移完成后，请删除或存档原始 HTML 文件以避免混淆。

