import json

d = json.load(open('public/data/brands.json', 'r', encoding='utf-8'))
brands = d['brands']

missing = []
has_en = []
for b in brands:
    if b['name'] == b['nameEn']:
        missing.append(b['name'])
    else:
        has_en.append(f"{b['name']} -> {b['nameEn']}")

print(f'Total brands: {len(brands)}')
print(f'Has English name: {len(has_en)}')
print(f'Missing English name: {len(missing)}')
print()
print('=== Missing English name brands ===')
for m in missing:
    print(f'  {m}')

print()
print('=== Sample model names (first 20) ===')
count = 0
for b in brands[:10]:
    for m in b['models'][:3]:
        print(f'  {b["nameEn"]}: {m["name"]}')
        if m['variants']:
            print(f'    variant: {m["variants"][0]["specName"]}')
        count += 1
        if count >= 20:
            break

