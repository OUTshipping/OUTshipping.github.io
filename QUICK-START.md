# 🚀 快速开始指南

本指南将帮助你在 5 分钟内启动 Triple Goats Vue 项目。

## 📋 前提条件

- ✅ Windows 10/11
- ✅ Node.js 16+ (下载: https://nodejs.org/)
- ✅ PowerShell

## 🎯 快速启动（3 步）

### 方法 1: 使用自动化脚本（推荐）

1. **运行设置脚本**
```powershell
.\setup.ps1
```

2. **启动开发服务器**
```powershell
.\start-dev.ps1
```

3. **在浏览器中打开**
```
http://localhost:3000
```

### 方法 2: 手动设置

1. **安装依赖**
```bash
npm install
```

2. **创建 public 目录并移动静态资源**
```powershell
# 创建目录
New-Item -ItemType Directory -Path public -Force

# 移动图片
Move-Item *.jpg,*.png,*.svg,*.ico,*.mp4 public/ -ErrorAction SilentlyContinue

# 移动文件夹
Move-Item bz3,C16,EV5,frontlander,id4crozz,seagull,songplus,V6E,yuanplus public/ -ErrorAction SilentlyContinue
```

3. **启动开发服务器**
```bash
npm run dev
```

## ✅ 验证安装

访问以下页面确保一切正常：

- ✓ 首页: http://localhost:3000/
- ✓ 关于我们: http://localhost:3000/about
- ✓ 库存: http://localhost:3000/inventory
- ✓ 联系我们: http://localhost:3000/contact

## 🛠️ 常用命令

```bash
# 开发环境
npm run dev          # 启动开发服务器

# 生产构建
npm run build        # 构建生产版本
npm run preview      # 预览生产构建

# 代码检查
npm run lint         # 运行代码检查（如果配置）
```

## 📂 项目结构速览

```
.
├── src/                # 源代码
│   ├── views/         # 页面组件
│   ├── components/    # 可复用组件
│   ├── router/        # 路由配置
│   └── assets/        # 资源文件
├── public/            # 静态资源（图片、视频等）
├── index.html         # HTML 模板
└── package.json       # 项目配置
```

## 🎨 修改内容

### 修改页面内容
编辑 `src/views/` 目录下的 `.vue` 文件

### 修改导航栏
编辑 `src/components/HeaderNav.vue`

### 修改全局样式
编辑 `src/assets/styles/global.css`

### 添加新页面
1. 在 `src/views/` 创建新的 `.vue` 文件
2. 在 `src/router/index.js` 添加路由

## 🐛 常见问题

### 问题: 端口已被占用
**解决方案**: 修改 `vite.config.js` 中的端口号
```js
server: {
  port: 3001  // 改为其他端口
}
```

### 问题: 图片不显示
**解决方案**: 确保图片在 `public/` 目录中，并使用 `/image.jpg` 路径引用

### 问题: npm install 慢
**解决方案**: 使用国内镜像
```bash
npm config set registry https://registry.npmmirror.com
npm install
```

## 📚 下一步

- 📖 阅读完整文档: `README-VUE.md`
- 🔄 查看迁移指南: `MIGRATION-GUIDE.md`
- 🌐 学习 Vue.js: https://cn.vuejs.org/

## 💡 开发技巧

1. **热重载**: 保存文件后页面自动刷新
2. **开发者工具**: 安装 Vue DevTools 浏览器插件
3. **代码编辑器**: 推荐使用 VS Code + Volar 插件

## 🆘 获取帮助

遇到问题？

1. 查看 `MIGRATION-GUIDE.md` 的常见问题章节
2. 检查浏览器控制台的错误信息
3. 搜索 Vue.js 官方文档

---

**提示**: 首次启动可能需要几分钟来安装依赖，请耐心等待。

Happy coding! 🎉

