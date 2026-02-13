# SEO 集群优化方案 — 完整交付文档

创建于：2025-02-13
项目：浙江阿啦丁集团三站 SEO 集群优化

---

## 一、zjaladin.com JSON-LD（部署到母公司站点 `<head>` 中）

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Corporation",
  "@id": "https://www.zjaladin.com/#corporation",
  "name": "浙江阿啦丁进出口贸易有限责任公司",
  "alternateName": ["Zhejiang Aladdin Import & Export Trading Co., Ltd.", "浙江阿啦丁", "Aladdin Group", "zjaladin"],
  "url": "https://www.zjaladin.com",
  "logo": "https://www.zjaladin.com/logo.png",
  "description": "中国浙江省汽车出口企业，专注新能源汽车及二手车全球供应链。旗下运营 AladinAuto 国际线上交易平台，并在非洲卢旺达设有子公司 TG Automobile 负责本地销售与售后。",
  "foundingDate": "2020",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "浙江省",
    "addressCountry": "CN"
  },
  "areaServed": {
    "@type": "Place",
    "name": "Global"
  },
  "subOrganization": [
    {
      "@type": "OnlineBusiness",
      "@id": "https://www.aladinauto.com/#platform",
      "name": "AladinAuto",
      "alternateName": "阿啦丁汽车",
      "url": "https://www.aladinauto.com",
      "description": "Global used car and new energy vehicle online export platform, direct from China"
    },
    {
      "@type": "AutoDealer",
      "@id": "https://tgautomobile.com/#autodealer",
      "name": "Triple Goats - T&G Automobile",
      "alternateName": "三羊汽车",
      "url": "https://tgautomobile.com",
      "description": "Rwanda subsidiary — local EV sales, after-sales service, and customs clearance in Kigali"
    }
  ],
  "owns": {
    "@type": "OnlineBusiness",
    "@id": "https://www.aladinauto.com/#platform",
    "name": "AladinAuto",
    "url": "https://www.aladinauto.com"
  },
  "sameAs": [
    "https://www.aladinauto.com",
    "https://tgautomobile.com"
  ]
}
</script>
```

---

## 二、aladinauto.com JSON-LD（部署到平台站点 `<head>` 中）

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["OnlineBusiness", "AutoDealer"],
  "@id": "https://www.aladinauto.com/#platform",
  "name": "AladinAuto",
  "alternateName": ["阿啦丁汽车", "Aladin Auto", "AladinAuto Global Used Car Platform"],
  "url": "https://www.aladinauto.com",
  "logo": "https://www.aladinauto.com/logo.png",
  "description": "AladinAuto is a global used car and new energy vehicle online export platform operated by Zhejiang Aladdin Group. We connect Chinese vehicle suppliers with international buyers across Africa, the Middle East, Southeast Asia, and South America.",
  "foundingDate": "2023",
  "areaServed": [
    {"@type": "Place", "name": "Africa"},
    {"@type": "Place", "name": "Middle East"},
    {"@type": "Place", "name": "Southeast Asia"},
    {"@type": "Place", "name": "South America"},
    {"@type": "Place", "name": "Central Asia"}
  ],
  "parentOrganization": {
    "@type": "Corporation",
    "@id": "https://www.zjaladin.com/#corporation",
    "name": "浙江阿啦丁进出口贸易有限责任公司",
    "alternateName": "Zhejiang Aladdin Import & Export Trading Co., Ltd.",
    "url": "https://www.zjaladin.com"
  },
  "department": {
    "@type": "AutoDealer",
    "@id": "https://tgautomobile.com/#autodealer",
    "name": "Triple Goats - T&G Automobile",
    "url": "https://tgautomobile.com",
    "description": "Our Rwanda delivery partner — handles local sales, customs clearance, and after-sales in Kigali"
  },
  "makesOffer": [
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Used Car Export from China"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "New Energy Vehicle Export"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "International Shipping & Logistics"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Vehicle Inspection & Certification"}}
  ],
  "sameAs": [
    "https://www.zjaladin.com",
    "https://tgautomobile.com"
  ]
}
</script>
```

---

## 三、aladinauto.com Meta Tags 消歧方案（部署到平台站点 `<head>` 中）

> 核心策略：在所有 meta 层强化 "Used Car Export" + "China Origin" + "Global Platform"，切断与 "Aladdin lamp / car wash" 的语义关联。

```html
<title>AladinAuto — Global Used Car & EV Export Platform | Direct from China | Zhejiang Aladdin Group</title>

<meta name="description" content="AladinAuto is a global used car and new energy vehicle export platform by Zhejiang Aladdin Group. Browse thousands of quality vehicles — sedans, SUVs, trucks, EVs — sourced and inspected in China, shipped worldwide to Africa, Middle East, and beyond. Not a lamp, not a car wash — we export real cars.">
<meta name="keywords" content="AladinAuto, Aladin Auto, used car export China, Chinese used car platform, new energy vehicle export, EV export from China, buy car from China, global car export, vehicle shipping China to Africa, Zhejiang Aladdin, 阿啦丁汽车, 浙江阿啦丁, 中国二手车出口, 新能源汽车出口, aladinauto.com, used car marketplace, auto export platform, China car dealer online, wholesale vehicles China">
<meta name="author" content="AladinAuto — A platform by Zhejiang Aladdin Import & Export Trading Co., Ltd.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.aladinauto.com/">



<!-- Hreflang: 关联站点路由 -->
<link rel="alternate" hreflang="en" href="https://www.aladinauto.com/">
<link rel="alternate" hreflang="zh" href="https://www.zjaladin.com/">
<link rel="alternate" hreflang="en-rw" href="https://tgautomobile.com/">
<link rel="alternate" hreflang="x-default" href="https://www.aladinauto.com/">

<!-- Open Graph（消歧重点：强调 automotive export） -->
<meta property="og:title" content="AladinAuto — Global Used Car & EV Export Platform from China">
<meta property="og:description" content="Not a lamp, not a car wash. AladinAuto is a professional automotive export platform by Zhejiang Aladdin Group. Quality used cars & new energy vehicles shipped from China to the world.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.aladinauto.com/">
<meta property="og:image" content="https://www.aladinauto.com/og-image.jpg">
<meta property="og:site_name" content="AladinAuto - Global Auto Export Platform">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="zh_CN">
<meta property="og:locale:alternate" content="fr_FR">
<meta property="og:locale:alternate" content="ar_SA">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="AladinAuto — Used Car & EV Export from China to the World">
<meta name="twitter:description" content="Global automotive export platform by Zhejiang Aladdin Group. Browse, order, and ship quality vehicles from China.">
<meta name="twitter:image" content="https://www.aladinauto.com/og-image.jpg">

<!-- 额外消歧信号 -->
<meta property="article:section" content="Automotive Export">
<meta property="article:tag" content="used car export, China auto, EV export, global car platform">
```

---

## 四、zjaladin.com / aladinauto.com 内链建议

### 4a. zjaladin.com 建议添加的内链（在 footer 或 About 页面）

```html
<!-- zjaladin.com footer 内链区块 -->
<div class="global-network">
  <h4>我们的全球网络</h4>
  <ul>
    <li>
      <a href="https://www.aladinauto.com" target="_blank" rel="noopener">AladinAuto 国际平台</a>
      <span>在线浏览并订购二手车与新能源汽车，从中国直接出口至全球</span>
    </li>
    <li>
      <a href="https://tgautomobile.com" target="_blank" rel="noopener">TG Automobile 卢旺达</a>
      <span>我们的非洲子公司，负责卢旺达本地销售、清关及售后服务</span>
    </li>
  </ul>
</div>
```

### 4b. aladinauto.com 建议添加的内链（在 footer 或 About 页面）

```html
<!-- aladinauto.com footer 内链区块 -->
<div class="global-network">
  <h4>Our Network</h4>
  <ul>
    <li>
      <a href="https://www.zjaladin.com" target="_blank" rel="noopener">Zhejiang Aladdin Group</a>
      <span>Our parent company — automotive supply chain headquarters in Zhejiang, China</span>
    </li>
    <li>
      <a href="https://tgautomobile.com" target="_blank" rel="noopener">TG Automobile Rwanda</a>
      <span>Our Africa delivery partner — local sales, customs clearance & after-sales in Kigali</span>
    </li>
  </ul>
</div>
```

### 内链合规要点

1. 所有跨站链接都出现在有实际用户价值的上下文中（带描述文字），不是裸链接堆砌
2. 使用 `target="_blank" rel="noopener"` 标记为外部链接，Google 不会将其视为操控性内链
3. 三站互链形成三角形而非单向链条，每个站点都有独立的内容价值
4. 链接锚文本使用品牌名+功能描述（如 "AladinAuto 国际平台"），而非关键词堆砌
5. 每个站点的 footer 只放 2 个关联链接，不过度互链

---

## 五、企业矩阵说明文案（约 300 字，中英双语）

### English Version（用于 aladinauto.com 和 tgautomobile.com 的 About Us）

Zhejiang Aladdin Import & Export Trading Co., Ltd. (浙江阿啦丁进出口贸易有限责任公司) is a Chinese automotive export corporation headquartered in Zhejiang Province, specializing in new energy vehicles and quality used cars for the global market. The Group operates an integrated supply chain that spans sourcing, inspection, online sales, international shipping, and local delivery.

AladinAuto (aladinauto.com) is the Group's international online platform, where buyers from Africa, the Middle East, Southeast Asia, and South America can browse thousands of vehicles — from compact EVs to heavy-duty trucks — and place orders for direct export from China. Every vehicle listed on AladinAuto undergoes a multi-point inspection before shipment.

In Rwanda, the Group's subsidiary Triple Goats — officially San Yang (Rwanda) Automobile Sales Co., Ltd., operating as T&G Automobile (tgautomobile.com) — handles the final mile. Based in Kigali's Kicukiro district, Triple Goats provides local vehicle registration, customs clearance, after-sales maintenance, EV charging, and on-the-ground customer support. Whether you discover a vehicle on AladinAuto or visit the Kigali showroom, you are backed by the same end-to-end network: from factory floor in China to your driveway in Africa.

### 中文版本（用于 zjaladin.com 的关于我们）

浙江阿啦丁进出口贸易有限责任公司是一家总部位于浙江省的汽车出口企业，专注于新能源汽车及优质二手车的全球供应链业务。集团构建了从车源采购、质量检测、线上销售、国际物流到本地交付的一体化服务体系。

AladinAuto（aladinauto.com）是集团旗下的国际线上交易平台，面向非洲、中东、东南亚及南美洲的买家，提供从紧凑型电动车到重型卡车的全品类车辆浏览与在线订购服务，所有上架车辆均经过多点检测后方可出口。

在非洲卢旺达，集团子公司三羊汽车（Triple Goats），即 San Yang (Rwanda) Automobile Sales Co., Ltd.，以 T&G Automobile（tgautomobile.com）品牌运营，负责最后一公里的本地化服务——包括车辆上牌、海关清关、售后维保、电动车充电及基加利地区的客户支持。无论您是在 AladinAuto 平台发现心仪车辆，还是直接走进基加利展厅，背后都是同一张从中国工厂到非洲家门口的完整服务网络。

---

## 六、sitemap 互引与 robots.txt 优化建议

### 6a. tgautomobile.com robots.txt（建议更新 public/robots.txt）

```
# Triple Goats - T&G Automobile
# https://tgautomobile.com
# A subsidiary of Zhejiang Aladdin Group

User-agent: *
Allow: /

# 关联站点声明（帮助爬虫理解集团关系）
# Parent: https://www.zjaladin.com
# Platform: https://www.aladinauto.com

Sitemap: https://tgautomobile.com/sitemap.xml
```

### 6b. zjaladin.com robots.txt 建议

```
User-agent: *
Allow: /

# Subsidiary sites
# Platform: https://www.aladinauto.com
# Rwanda: https://tgautomobile.com

Sitemap: https://www.zjaladin.com/sitemap.xml
```

### 6c. aladinauto.com robots.txt 建议

```
User-agent: *
Allow: /

# Parent: https://www.zjaladin.com
# Rwanda delivery: https://tgautomobile.com

Sitemap: https://www.aladinauto.com/sitemap.xml
```

### 6d. sitemap 互引说明

Google 不支持在 sitemap 中直接引用其他域名的 URL。正确的做法是：
1. 每个站点维护自己的 sitemap.xml，只包含自己域名下的 URL
2. 通过 JSON-LD 的 `@id` 互相引用建立实体关联（已在上面的代码中实现）
3. 通过 Google Search Console 将三个站点关联到同一个 Google 账号下
4. 在 Google Search Console 中为每个站点提交各自的 sitemap