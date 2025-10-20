# Triple Goats Vue 项目

这是将 Triple Goats 网站从 HTML 转换为 Vue.js 的项目。

## 项目结构

```
.
├── src/
│   ├── assets/
│   │   └── styles/
│   │       └── global.css          # 全局样式
│   ├── components/
│   │   ├── HeaderNav.vue           # 导航栏组件
│   │   ├── FooterBar.vue           # 页脚组件
│   │   ├── SocialMedia.vue         # 社交媒体组件
│   │   └── ContactInfo.vue         # 联系信息组件
│   ├── views/
│   │   ├── HomeView.vue            # 首页
│   │   ├── AboutView.vue           # 关于我们
│   │   ├── InventoryView.vue       # 库存页面
│   │   ├── ContactView.vue         # 联系我们
│   │   ├── ServicesView.vue        # 服务页面
│   │   ├── ChargingView.vue        # 充电站页面
│   │   ├── TestDriveView.vue       # 试驾预约
│   │   ├── RentalView.vue          # 租车服务
│   │   ├── TaxiView.vue            # 出租车服务
│   │   ├── SUVView.vue             # SUV页面
│   │   └── vehicles/               # 车辆详情页
│   │       ├── SongPlusView.vue
│   │       ├── BYDSeagullView.vue
│   │       └── ...
│   ├── router/
│   │   └── index.js                # 路由配置
│   ├── App.vue                     # 根组件
│   └── main.js                     # 入口文件
├── public/                         # 静态资源（图片、视频等）
├── vue-index.html                  # Vue 项目的 HTML 模板
├── package.json                    # 项目依赖
├── vite.config.js                  # Vite 配置
└── README-VUE.md                   # 本文件

```

## 功能特性

- ✅ Vue 3 Composition API
- ✅ Vue Router 4 路由管理
- ✅ 响应式设计（支持移动端和桌面端）
- ✅ 组件化开发
- ✅ 库存筛选和排序功能
- ✅ 车辆详情页面
- ✅ 联系表单和地图集成
- ✅ 社交媒体链接

## 安装步骤

### 1. 安装依赖

```bash
npm install
```

### 2. 将静态资源移动到 public 目录

需要将以下文件移动到 `public/` 目录：
- 所有图片文件（.jpg, .png, .svg 等）
- 视频文件（movie.mp4）
- 图标文件（favicon.ico, apple-touch-icon.png 等）
- 车辆图片文件夹（bz3/, C16/, EV5/ 等）

```bash
# Windows PowerShell
Move-Item -Path *.jpg,*.png,*.svg,*.ico,*.mp4,*.webmanifest,bz3,C16,EV5,frontlander,id4crozz,seagull,songplus,V6E,yuanplus -Destination public/ -Force
```

### 3. 启动开发服务器

```bash
npm run dev
```

项目将在 `http://localhost:3000` 运行

### 4. 构建生产版本

```bash
npm run build
```

构建后的文件将在 `dist/` 目录中

### 5. 预览生产构建

```bash
npm run preview
```

## 主要改进

### 与原 HTML 版本相比的优势：

1. **组件化**：将重复的代码（如导航栏、页脚）提取为可复用组件
2. **路由管理**：使用 Vue Router 实现单页应用（SPA），无需页面刷新
3. **状态管理**：在 InventoryView 中使用响应式数据管理车辆筛选和排序
4. **更好的代码组织**：按功能模块组织代码，易于维护和扩展
5. **开发体验**：热模块替换（HMR），修改代码立即看到效果

## 路由说明

- `/` 或 `/home` - 首页
- `/about` - 关于我们
- `/inventory` - 库存页面（支持 ?type=suv 等查询参数）
- `/contact` - 联系我们
- `/services` - 服务页面
- `/charging` - 充电站页面
- `/testdrive` - 试驾预约
- `/rental` - 租车服务
- `/taxi` - 出租车服务
- `/suv` - SUV 页面
- `/song-plus` - BYD Song Plus 详情页
- `/byd-seagull` - BYD Seagull 详情页
- 其他车辆详情页...

## 技术栈

- **Vue 3** - 渐进式 JavaScript 框架
- **Vue Router 4** - 官方路由管理器
- **Vite** - 下一代前端构建工具
- **CSS3** - 样式和动画

## 待完善功能

目前车辆详情页为占位符页面，需要根据原 HTML 文件完善以下内容：
- 车辆详细信息展示
- 车辆图片轮播
- 规格参数表
- 在线询价功能

## 注意事项

1. 确保所有静态资源（图片、视频）都在 `public/` 目录中
2. 开发时使用 `npm run dev`，不要直接打开 HTML 文件
3. 如需修改样式，可以在各组件的 `<style scoped>` 中修改，或在 `global.css` 中修改全局样式
4. 路由使用 HTML5 History 模式，部署时需要配置服务器重定向

## 联系方式

如有问题，请联系：
- Email: tgautomobilee@gmail.com
- Phone: +250 785 084 313 / +250 794 104 908

