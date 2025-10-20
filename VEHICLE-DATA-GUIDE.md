# 车辆详情数据更新指南

## ✅ 已完成

- **ID.4 Crozz** - 已添加完整的车辆详情、图片轮播和规格信息

## 🎯 如何为其他车辆添加详情

### 方法 1: 手动从 HTML 文件提取数据

1. 打开 `html-backup/` 目录中对应的 HTML 文件
2. 找到车辆信息部分（在 `<main>` 标签内）
3. 复制以下信息：
   - 车辆名称（`<h2>` 标签）
   - 车辆描述（`vehicle-description` 中的 `<p>` 标签）
   - 规格表格数据（`<table>` 内容）
   - 图片路径（`<img src="">` 属性）
   - 颜色选项（`color-circle` 的 `style` 属性）

4. 更新对应的 Vue 文件（在 `src/views/vehicles/` 目录）

### 示例：更新 BYD Seagull

1. **读取原始数据**
   - 打开 `html-backup/byd-seagull.html`
   - 找到车辆信息

2. **更新 Vue 文件**
   编辑 `src/views/vehicles/BYDSeagullView.vue`:

```vue
<template>
  <VehicleDetail
    :vehicle-name="vehicleData.name"
    :description="vehicleData.description"
    :specs="vehicleData.specs"
    :images="vehicleData.images"
    :colors="vehicleData.colors"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'

const vehicleData = {
  name: '2024 BYD Seagull',  // 从 HTML 的 <h2> 获取
  description: '车辆描述内容...',  // 从 HTML 的 vehicle-description 获取
  specs: {
    year: '2024',
    make: 'BYD',
    model: 'Seagull',
    range: '300',  // 从表格获取
    seats: '5',
    category: 'PASSENGER',
    batteryCapacity: '30.08 kWh'  // 从表格获取
  },
  images: [
    '/seagull/SEAGULL (1).jpg',  // 图片路径，记得添加前缀 /
    '/seagull/SEAGULL (2).jpg',
    '/seagull/SEAGULL (3).jpg',
    '/seagull/SEAGULL (4).jpg',
    '/seagull/SEAGULL (5).jpg',
    '/seagull/SEAGULL (6).jpg',
    '/seagull/SEAGULL (7).jpg'
  ],
  colors: ['#000000', '#FFFFFF']  // 从 color-circle 的 style 获取
}
</script>
```

### 需要更新的车辆列表

在 `src/views/vehicles/` 目录下的以下文件：

- [ ] BYDSeagullView.vue
- [ ] BYDYuanPlusView.vue
- [ ] FarizonV6EView.vue
- [x] ID4CrozzView.vue ✅
- [ ] KIAEV5View.vue
- [ ] LeapmotorC16View.vue
- [ ] SongPlusView.vue
- [ ] ToyotaBZ3View.vue
- [ ] ToyotaFrontlanderView.vue
- [ ] ToyotaHighlandView.vue

### 对应的 HTML 文件（在 html-backup/ 目录）

```
byd-seagull.html          -> BYDSeagullView.vue
byd-yuan-plus.html        -> BYDYuanPlusView.vue
farizon-v6e.html          -> FarizonV6EView.vue
id4-crozz.html            -> ID4CrozzView.vue ✅
kia-ev5.html              -> KIAEV5View.vue
leapmotor-c16.html        -> LeapmotorC16View.vue
song-plus.html            -> SongPlusView.vue
toyota-bz3.html           -> ToyotaBZ3View.vue
toyota-corolla-cross-frontlander.html -> ToyotaFrontlanderView.vue
toyota-corolla-cross-highland.html    -> ToyotaHighlandView.vue
```

## 🔧 快速提取数据的技巧

### 1. 提取车辆名称
在 HTML 文件中搜索：`<h2>` 标签

### 2. 提取描述
在 HTML 文件中搜索：`vehicle-description` 类名

### 3. 提取规格表格
在 HTML 文件中找到 `<tbody>` 标签，提取：
- YEAR
- MAKE
- MODEL
- RANGE
- SEATS
- CATEGORY
- BATTERY CAPACITY

### 4. 提取图片路径
在 HTML 文件中搜索：`carousel-slide` 内的 `<img src="">`
**重要**：图片路径需要添加前缀 `/`，例如：
- 原始：`seagull\SEAGULL (1).jpg`
- 转换为：`/seagull/SEAGULL (1).jpg`

### 5. 提取颜色
在 HTML 文件中搜索：`color-circle` 的 `style` 属性
例如：`style="background-color: #000000;"`

## 📝 模板代码

你可以复制以下模板，然后替换数据：

```vue
<template>
  <VehicleDetail
    :vehicle-name="vehicleData.name"
    :description="vehicleData.description"
    :specs="vehicleData.specs"
    :images="vehicleData.images"
    :colors="vehicleData.colors"
  />
</template>

<script setup>
import VehicleDetail from '@/components/VehicleDetail.vue'

const vehicleData = {
  name: '',  // 车辆名称
  description: '',  // 车辆描述
  specs: {
    year: '',
    make: '',
    model: '',
    range: '',
    seats: '',
    category: '',
    batteryCapacity: ''
  },
  images: [
    // 图片路径数组
  ],
  colors: [
    // 颜色数组，格式：'#000000'
  ]
}
</script>
```

## 🎯 测试

更新车辆数据后：

1. 保存文件
2. 开发服务器会自动重新加载
3. 访问对应的车辆详情页：
   - http://localhost:3002/id4-crozz ✅
   - http://localhost:3002/byd-seagull
   - http://localhost:3002/song-plus
   - 等等...

## 💡 提示

- 图片路径必须以 `/` 开头
- 颜色代码使用十六进制格式：`#RRGGBB`
- 确保图片文件在 `public/` 目录中
- 如果图片不显示，检查路径中的 `\` 是否改为了 `/`

## 🆘 需要帮助？

如果你需要我帮你提取某个特定车辆的数据，请告诉我车辆名称，我可以帮你从 HTML 文件中提取数据并生成完整的 Vue 代码。

