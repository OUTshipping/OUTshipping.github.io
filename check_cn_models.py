import json

d = json.load(open('public/data/brands.json', 'r', encoding='utf-8'))
brands = d['brands']

cn_models = []
for b in brands:
    for m in b['models']:
        me = m.get('nameEn', '')
        if any('\u4e00' <= c <= '\u9fff' for c in me):
            cn_models.append(f"  [{b['nameEn']}] {m['name']} -> {me}")

print(f"Models with CN in nameEn: {len(cn_models)}")
for s in cn_models:
    print(s)

