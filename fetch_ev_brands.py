"""
新能源车型数据爬虫 — 从汽车之家爬取新能源品牌/车系/配置数据
输出：public/data/brands.json
用法：python -u fetch_ev_brands.py
"""
import sys
import re
import json
import os
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 强制 stdout 不缓冲
sys.stdout.reconfigure(line_buffering=True)

# ============ 常量与配置 ============

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "public", "data", "brands.json")

# 品牌中文→英文名映射
BRAND_EN_MAP = {
    "比亚迪": "BYD", "特斯拉": "Tesla", "蔚来": "NIO", "小鹏": "XPeng",
    "理想": "Li Auto", "极氪": "Zeekr", "吉利": "Geely", "长安": "Changan",
    "长城": "Great Wall", "广汽": "GAC", "上汽": "SAIC", "奇瑞": "Chery",
    "哪吒": "Nezha", "零跑": "Leapmotor", "岚图": "Voyah", "阿维塔": "Avatr",
    "智己": "IM Motors", "飞凡": "Rising", "高合": "HiPhi", "极狐": "Arcfox",
    "欧拉": "ORA", "几何": "Geometry", "埃安": "Aion", "深蓝": "Deepal",
    "方程豹": "Fangchengbao", "仰望": "Yangwang", "腾势": "Denza",
    "启辰": "Venucia", "红旗": "Hongqi", "东风": "Dongfeng", "北汽": "BAIC",
    "五菱": "Wuling", "宝骏": "Baojun", "名爵": "MG", "荣威": "Roewe",
    "传祺": "Trumpchi", "领克": "Lynk & Co", "魏牌": "Wey", "星途": "Exeed",
    "捷途": "Jetour", "创维": "Skyworth", "威马": "WM Motor", "大众": "Volkswagen",
    "宝马": "BMW", "奔驰": "Mercedes-Benz", "奥迪": "Audi", "丰田": "Toyota",
    "本田": "Honda", "日产": "Nissan", "现代": "Hyundai", "起亚": "Kia",
    "福特": "Ford", "雪佛兰": "Chevrolet", "别克": "Buick", "沃尔沃": "Volvo",
    "捷豹": "Jaguar", "路虎": "Land Rover", "保时捷": "Porsche",
    "林肯": "Lincoln", "凯迪拉克": "Cadillac", "雷克萨斯": "Lexus",
    "英菲尼迪": "Infiniti", "smart": "Smart", "MINI": "MINI",
    "极越": "Jiyue", "小米": "Xiaomi", "鸿蒙智行": "Harmony",
    "银河": "Galaxy", "iCAR": "iCAR", "昊铂": "Hyper",
    "远航": "Yuanhang", "合创": "Hycan", "睿蓝": "Ruilan",
    "云度": "Yudo", "天际": "Enovate", "爱驰": "Aiways",
}

# 车身结构中文→英文类型映射
BODY_TYPE_MAP = {
    "SUV": "SUV", "轿车": "SEDAN", "MPV": "VAN", "皮卡": "PICKUP",
    "跑车": "SEDAN", "微型车": "SEDAN", "小型车": "SEDAN",
    "中型车": "SEDAN", "大型车": "SEDAN", "紧凑型车": "SEDAN",
    "中大型车": "SEDAN", "微卡": "TRUCK", "轻卡": "TRUCK",
    "中卡": "TRUCK", "重卡": "TRUCK",
}

# 预编译正则
RE_DOC_WRITELN = re.compile(r'document\.writeln\("(.*)"\)')
RE_SERIES_ID = re.compile(r'/price/series-(\d+)\.html')
RE_BRAND_INFO = re.compile(r'<a href=([^>]*?)><i[^>]*?></i>([^<]+)<em>')
RE_BRAND_ID = re.compile(r'/price/brand-(\d+)\.html')

# ============ API 请求函数 ============

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch(url, params=None, retries=3, timeout=15):
    """带重试的 GET 请求（禁用 SSL 验证以兼容代理/VPN 环境）"""
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, params=params,
                             timeout=timeout, verify=False)
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            if attempt == retries - 1:
                print(f"  [错误] 请求失败: {e}")
                return None
            time.sleep(2)
    return None


def get_all_brands():
    """获取全部品牌列表：返回 [(brand_id, brand_name), ...]"""
    r = fetch("https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx",
              {"typeId": "1", "brandId": "0", "fctId": "0", "seriesId": "0"})
    if not r:
        return []
    matches = RE_BRAND_INFO.findall(r.text)
    brands = []
    for href, name in matches:
        bid = RE_BRAND_ID.search(href)
        if bid:
            brands.append((bid.group(1), name.strip()))
    return brands


def get_series_for_brand(brand_id):
    """获取某品牌下全部车系：返回 [(series_id, series_name), ...]"""
    r = fetch("https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx",
              {"typeId": "1", "brandId": brand_id, "fctId": "0", "seriesId": "0"})
    if not r:
        return []
    html_m = RE_DOC_WRITELN.search(r.text)
    if not html_m:
        return []
    soup = BeautifulSoup(html_m.group(1), "html.parser")
    links = soup.select(".current > dl > dd > a")
    series = []
    for link in links:
        sname = link.contents[0].text.strip()
        sid = RE_SERIES_ID.search(link.get("href", ""))
        if sid:
            series.append((sid.group(1), sname))
    return series




def get_series_config(series_id):
    """获取某车系的配置数据，返回 JSON dict 或 None"""
    r = fetch("https://car-web-api.autohome.com.cn/car/param/getParamConf",
              {"mode": "1", "site": "1", "seriesid": series_id})
    if not r:
        return None
    try:
        data = json.loads(r.text)
        if data.get("returncode") != 0:
            return None
        return data.get("result", {})
    except (json.JSONDecodeError, KeyError):
        return None


def extract_ev_variants(result):
    """
    从配置 API 结果中提取新能源车型变体。
    只保留有纯电续航里程且 > 0 的车型。
    返回 [variant_dict, ...] 或空列表
    """
    datalist = result.get("datalist", [])
    titlelist = result.get("titlelist", [])
    if not datalist or not titlelist:
        return []

    # 建立配置项名称到全局索引的映射
    item_name_to_index = {}
    idx = 0
    for title in titlelist:
        for item in title.get("items", []):
            name = item.get("itemname", "").strip()
            if name:
                item_name_to_index[name] = idx
            idx += 1

    # 找到关键字段的索引
    def find_index(*keywords):
        for k in keywords:
            for name, i in item_name_to_index.items():
                if k in name:
                    return i
        return -1

    idx_range = find_index("纯电续航里程(km)", "纯电续航里程")
    idx_seats = find_index("座位数")
    idx_battery = find_index("电池容量(kWh)", "电池容量")
    idx_body = find_index("车身结构")
    idx_year = find_index("年款")

    if idx_range < 0:
        # 没有纯电续航字段 -> 非新能源车系
        return []

    variants = []
    for car in datalist:
        plist = car.get("paramconflist", [])
        spec_name = car.get("specname", "") or car.get("name", "")

        # 获取续航
        ev_range = 0
        if idx_range < len(plist):
            raw = plist[idx_range].get("itemname", "")
            nums = re.findall(r"[\d.]+", raw)
            if nums:
                ev_range = int(float(nums[0]))
        if ev_range <= 0:
            continue  # 跳过非纯电配置

        # 获取座位数
        seats = 5
        if idx_seats >= 0 and idx_seats < len(plist):
            raw = plist[idx_seats].get("itemname", "")
            nums = re.findall(r"\d+", raw)
            if nums:
                seats = int(nums[0])

        # 获取电池容量
        battery = "N/A"
        if idx_battery >= 0 and idx_battery < len(plist):
            raw = plist[idx_battery].get("itemname", "")
            if raw and raw != "-":
                battery = raw.strip() + (" kWh" if "kWh" not in raw else "")

        # 获取车身结构
        body_type = "SUV"
        if idx_body >= 0 and idx_body < len(plist):
            raw = plist[idx_body].get("itemname", "").strip()
            for cn, en in BODY_TYPE_MAP.items():
                if cn in raw:
                    body_type = en
                    break

        # 获取年款
        year = "2025"
        if idx_year >= 0 and idx_year < len(plist):
            raw = plist[idx_year].get("itemname", "")
            nums = re.findall(r"\d{4}", raw)
            if nums:
                year = nums[0]

        variants.append({
            "specName": spec_name,
            "year": year,
            "type": body_type,
            "range": ev_range,
            "seats": seats,
            "batteryCapacity": battery,
        })

    return variants


# ============ 主流程 ============

def main():
    print("=" * 60)
    print("  新能源车型数据爬虫 -- 汽车之家")
    print("=" * 60)

    # 1. 获取全部品牌
    print("\n[1/3] 获取品牌列表...")
    all_brands = get_all_brands()
    print(f"  共 {len(all_brands)} 个品牌")

    # 2. 遍历品牌，获取车系和配置
    print("\n[2/3] 遍历品牌，获取新能源车系配置...")
    brands_result = []
    total_models = 0
    total_variants = 0

    for bi, (brand_id, brand_name) in enumerate(all_brands, 1):
        brand_en = BRAND_EN_MAP.get(brand_name, brand_name)
        print(f"\n  [{bi}/{len(all_brands)}] {brand_name} ({brand_en})")

        series_list = get_series_for_brand(brand_id)
        if not series_list:
            print(f"    跳过 -- 无车系")
            continue

        models = []
        for si, (series_id, series_name) in enumerate(series_list, 1):
            print(f"    [{si}/{len(series_list)}] {series_name}...", end=" ")
            config = get_series_config(series_id)
            if not config:
                print("无配置数据")
                time.sleep(0.3)
                continue

            variants = extract_ev_variants(config)
            if not variants:
                print("非新能源/无纯电续航")
                time.sleep(0.3)
                continue

            print(f"找到 {len(variants)} 个新能源配置")
            models.append({
                "name": series_name,
                "variants": variants,
            })
            total_variants += len(variants)
            time.sleep(0.5)  # 控制请求频率

        if models:
            brands_result.append({
                "name": brand_name,
                "nameEn": brand_en,
                "models": models,
            })
            total_models += len(models)
            print(f"  -> {brand_name}: {len(models)} 个新能源车系")

        time.sleep(0.3)

    # 3. 保存 JSON
    print(f"\n[3/3] 保存数据...")
    output = {
        "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
        "brands": brands_result,
    }
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n{'=' * 60}")
    print(f"  完成! 共 {len(brands_result)} 个品牌, {total_models} 个车系, {total_variants} 个配置")
    print(f"  数据已保存到: {OUTPUT_PATH}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()