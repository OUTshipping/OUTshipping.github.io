import json

d = json.load(open('public/data/brands.json', 'r', encoding='utf-8'))
brands = d['brands']

# 检查还有没有品牌 nameEn 仍然是中文
still_cn = []
for b in brands:
    if any('\u4e00' <= c <= '\u9fff' for c in b['nameEn']):
        still_cn.append(f"  {b['name']} -> {b['nameEn']}")

print(f"Total brands: {len(brands)}")
print(f"Brands with Chinese in nameEn: {len(still_cn)}")
if still_cn:
    for s in still_cn:
        print(s)

# 抽查几个关键品牌
print("\n=== Key brands check ===")
key_names = ["比亚迪", "特斯拉", "小米汽车", "众泰", "标致", "兰博基尼", "宾利", "哈弗", "坦克", "乐道"]
for kn in key_names:
    b = next((b for b in brands if b['name'] == kn), None)
    if b:
        print(f"  {b['name']} -> {b['nameEn']}")
        if b['models']:
            m = b['models'][0]
            print(f"    model: {m['name']} -> {m.get('nameEn','?')}")
            if m['variants']:
                v = m['variants'][0]
                print(f"    variant: {v['specName']} -> {v.get('specNameEn','?')}")

# 检查还有多少 model/variant 的英文名包含中文
cn_models = 0
cn_specs = 0
total_models = 0
total_specs = 0
for b in brands:
    for m in b['models']:
        total_models += 1
        me = m.get('nameEn', '')
        if any('\u4e00' <= c <= '\u9fff' for c in me):
            cn_models += 1
        for v in m['variants']:
            total_specs += 1
            se = v.get('specNameEn', '')
            if any('\u4e00' <= c <= '\u9fff' for c in se):
                cn_specs += 1

print(f"\n=== Translation coverage ===")
print(f"Models with CN in nameEn: {cn_models}/{total_models}")
print(f"Specs with CN in specNameEn: {cn_specs}/{total_specs}")

