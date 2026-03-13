# Triple Goats — T&G Automobile Rwanda

> Rwanda's trusted electric vehicle & used car dealer in Kigali, a subsidiary of [Zhejiang Aladdin Group](https://www.zjaladin.com).

🌐 **Live Site:** [tgautomobile.com](https://tgautomobile.com)

---

## About

Triple Goats (T&G Automobile) is a Kigali-based automotive dealer specializing in new energy vehicles and quality used cars sourced directly from China. We offer BYD, Dongfeng, Leapmotor, Kia, Toyota EVs and certified pre-owned vehicles, backed by full after-sales support, EV charging infrastructure, and customs clearance services.

### Our Global Network

| Entity | Role | Website |
|--------|------|---------|
| **Zhejiang Aladdin Group** | China HQ — Source & Export | [zjaladin.com](https://www.zjaladin.com) |
| **AladinAuto Platform** | Global Online Inventory | [aladinauto.com](https://www.aladinauto.com) |
| **T&G Automobile Rwanda** | Local Sales & Service | [tgautomobile.com](https://tgautomobile.com) |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | [Vue 3](https://vuejs.org/) (Composition API + `<script setup>`) |
| Build Tool | [Vite 5](https://vitejs.dev/) |
| SSG | [vite-ssg](https://github.com/antfu/vite-ssg) — Static Site Generation |
| Router | [Vue Router 4](https://router.vuejs.org/) |
| SEO | [@unhead/vue](https://unhead.unjs.io/) — Per-page `<head>` management |
| Icons | [Font Awesome 5](https://fontawesome.com/) |
| Font | [Inter](https://fonts.google.com/specimen/Inter) (Google Fonts) |
| Hosting | [GitHub Pages](https://pages.github.com/) |
| CI/CD | GitHub Actions — Auto deploy on push to `source` branch |

---

## Project Structure

```
├── .github/workflows/
│   └── deploy.yml              # GitHub Actions: build & deploy
├── public/
│   ├── data/
│   │   ├── vehicles.json       # Vehicle inventory data
│   │   └── brands.json         # Brand configuration
│   ├── images/
│   │   ├── pages/              # Page background images (about, contact, etc.)
│   │   ├── icons/              # UI icons (location, phone, time)
│   │   ├── social/             # Social media icons (facebook, ins, tiktok)
│   │   ├── categories/         # Vehicle category images (sedan, suv, truck, etc.)
│   │   └── vehicles/           # Vehicle photos (cover + detail per model)
│   │       ├── songplus/
│   │       ├── v6e/
│   │       ├── ev5/
│   │       └── ...             # 16 vehicle folders
│   ├── video/
│   │   ├── movie.mp4           # Homepage hero video
│   │   └── taxi.mp4            # Taxi page video
│   ├── companylogo.jpg         # Company logo
│   ├── sitemap.xml             # SEO sitemap
│   └── robots.txt              # Crawler directives
├── src/
│   ├── assets/styles/
│   │   └── global.css          # CSS variables & global styles
│   ├── components/
│   │   ├── HeaderNav.vue       # Navigation (desktop + mobile)
│   │   ├── PageLayout.vue      # Layout wrapper + WhatsApp FAB
│   │   ├── FooterBar.vue       # Footer with contact & links
│   │   ├── HeroSection.vue     # Reusable hero banner
│   │   ├── ContactInfo.vue     # CTA section
│   │   ├── SocialMedia.vue     # Social media links
│   │   └── VehicleDetail.vue   # Vehicle detail component
│   ├── views/                  # Page components
│   ├── router/index.js         # Route definitions
│   ├── main.js                 # Entry point (vite-ssg)
│   └── App.vue                 # Root component
├── index.html                  # HTML entry with SEO & JSON-LD
├── vite.config.js              # Vite configuration
└── package.json
```

---

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) >= 20
- npm >= 10

### Development

```bash
# Install dependencies
npm install

# Start dev server (http://localhost:5173)
npm run dev
```

### Build

```bash
# Build for production (SSG)
npm run build

# Preview production build
npx serve dist -l 4173
```

---

## Deployment

Fully automated via GitHub Actions:

1. Push to `source` branch
2. GitHub Actions runs `npm ci && npm run build`
3. `dist/` deployed to `main` branch (GitHub Pages)
4. Live at [tgautomobile.com](https://tgautomobile.com)

---

## Pages

| Route | Description |
|-------|-------------|
| `/home` | Homepage — Hero video, vehicle categories, map |
| `/inventory` | Vehicle inventory with filters |
| `/vehicle/:slug` | Dynamic vehicle detail pages |
| `/charging` | EV charging station info |
| `/services` | Services overview |
| `/testdrive` | Schedule a test drive |
| `/taxi` | Electric taxi service |
| `/rental` | EV car rental |
| `/about` | Company story & team |
| `/contact` | Contact info, map, hours |

---

## Contact

- **Address:** KK 15 Rd, Kicukiro District, Kigali, Rwanda
- **Phone:** +250 785 084 313 / +250 794 104 908
- **Email:** tgautomobile@gmail.com
- **Instagram:** [@tg_auto_rwanda](https://www.instagram.com/tg_auto_rwanda/)
- **Facebook:** [TripleGoats](https://www.facebook.com/TripleGoats)
- **Twitter:** [@Triple_Goats](https://x.com/Triple_Goats)
- **TikTok:** [@tg.auto.rwanda](https://www.tiktok.com/@tg.auto.rwanda)

---

## License

© 2025 Triple Goats - T&G Automobile. All rights reserved.

A subsidiary of [Zhejiang Aladdin Import & Export Trading Co., Ltd.](https://www.zjaladin.com)