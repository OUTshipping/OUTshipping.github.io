"""
品牌/车系/配置名称英文化脚本
读取 public/data/brands.json，为每个品牌/车系/配置生成英文名，写回 JSON
用法：python translate_brands.py
"""
import json
import os
import re

INPUT_PATH = os.path.join(os.path.dirname(__file__), "public", "data", "brands.json")

# ============================================================
# 完整品牌中英映射表 (覆盖全部253个新能源品牌)
# ============================================================
BRAND_EN_MAP = {
    # --- A ---
    "AITO 问界": "AITO",
    "ARCFOX极狐": "ARCFOX",
    "阿维塔": "Avatr",
    "阿斯顿·马丁": "Aston Martin",
    "阿斯顿・马丁": "Aston Martin",
    "爱驰": "Aiways",
    "安凯客车": "Ankai",
    "安徽猎豹": "Anhui Leopard",
    "奥迪": "Audi",
    "奥迪AUDI": "Audi",
    # --- B ---
    "比亚迪": "BYD",
    "宝马": "BMW",
    "奔驰": "Mercedes-Benz",
    "别克": "Buick",
    "保时捷": "Porsche",
    "宝骏": "Baojun",
    "北汽新能源": "BAIC NEV",
    "北汽昌河": "BAIC Changhe",
    "北汽瑞翔": "BAIC Ruixiang",
    "北汽": "BAIC",
    "北京汽车": "Beijing Auto",
    "北京汽车制造厂": "BAW",
    "北京越野": "Beijing Offroad",
    "本田": "Honda",
    "宾利": "Bentley",
    "奔腾": "Bestune",
    "宝沃": "Borgward",
    "百智新能源": "Baizhi NEV",
    "比克汽车": "Bike Auto",
    "比德文汽车": "Bidewen",
    # --- C ---
    "长安": "Changan",
    "长城": "Great Wall",
    "长安凯程": "Changan Kaicheng",
    "长安启源": "Changan Qiyuan",
    "长安欧尚": "Changan Oshan",
    "长安跨越": "Changan Kuayue",
    "传祺": "Trumpchi",
    "创维": "Skyworth",
    "创维汽车": "Skyworth Auto",
    "成功汽车": "Chenggong Auto",
    "春风": "CFMoto",
    "凯翼": "Cowin",
    "凯翼汽车": "Cowin Auto",
    "凯马": "Kaima",
    "凯迪拉克": "Cadillac",
    "克莱斯勒": "Chrysler",
    "克蒂汽车": "Kandi",
    "曹操汽车": "CaoCao Auto",
    # --- D ---
    "大众": "Volkswagen",
    "东风": "Dongfeng",
    "东风·瑞泰特": "Dongfeng Ruitaite",
    "东风・瑞泰特": "Dongfeng Ruitaite",
    "东风奕派": "Dongfeng Yipai",
    "东风富康": "Dongfeng Fukang",
    "东风小康": "Dongfeng Xiaokang",
    "东风御风": "Dongfeng Yufeng",
    "东风风光": "Dongfeng Fengguang",
    "东风风神": "Dongfeng Aeolus",
    "东风风行": "Dongfeng Fengxing",
    "东南": "Soueast",
    "DS": "DS",
    "大运": "Dayun",
    "大通": "Maxus",
    "大乘汽车": "Dacheng Auto",
    "大力牛魔王": "Bull Demon King",
    "电动屋": "Electric House",
    "电咖": "Dianka",
    "深蓝": "Deepal",
    "深蓝汽车": "Deepal",
    # --- E/F ---
    "飞凡": "Rising",
    "丰田": "Toyota",
    "福特": "Ford",
    "福田": "Foton",
    "法拉利": "Ferrari",
    "方程豹": "Fangchengbao",
    "飞碟汽车": "Feidie Auto",
    "富古汽车": "Fugu Auto",
    "前途": "Qiantu",
    "firefly萤火虫": "Firefly",
    # --- G ---
    "广汽": "GAC",
    "广汽传祺": "GAC Trumpchi",
    "广汽昊铂": "GAC Hyper",
    "广汽集团": "GAC Group",
    "吉利": "Geely",
    "吉利几何": "Geometry",
    "吉利汽车": "Geely Auto",
    "吉利银河": "Geely Galaxy",
    "吉利雷达": "Geely Radar",
    "吉祥汽车": "Jixiang Auto",
    "高合": "HiPhi",
    "高合汽车": "HiPhi",
    "国吉商用车": "Guoji Commercial",
    "国机智骏": "Guoji Zhijun",
    "国金汽车": "Guojin Auto",
    "全球鹰": "Gleagle",
    # --- H ---
    "红旗": "Hongqi",
    "哈弗": "Haval",
    "海马": "Haima",
    "海格": "Higer",
    "合创": "Hycan",
    "合创汽车": "Hycan",
    "恒天": "Hengtian",
    "恒润汽车": "Hengrun Auto",
    "恒驰": "Hengchi",
    "华东汽车": "Huadong Auto",
    "华凯": "Huakai",
    "华晨新日": "Huachen Xinri",
    "华梓汽车": "Huazi Auto",
    "华泰新能源": "Huatai NEV",
    "华骐": "Huaqi",
    "宏远汽车": "Hongyuan Auto",
    "黄海": "Huanghai",
    "货拉拉多拉汽车": "Huolala Dora",
    "昊铂": "Hyper",
    "鸿蒙智行": "Harmony",
    # --- I/J ---
    "iCAR": "iCAR",
    "Jeep": "Jeep",
    "捷豹": "Jaguar",
    "江淮汽车": "JAC",
    "江淮瑞风": "JAC Refine",
    "江淮钇为": "JAC Yiwei",
    "江汽集团": "JAC Group",
    "江铃": "JMC",
    "江铃晶马汽车": "JMC Jingma",
    "江铃集团新能源": "JMC NEV",
    "江南汽车": "Jiangnan Auto",
    "捷途山海": "Jetour Shanhai",
    "捷途纵横": "Jetour Zongheng",
    "捷途": "Jetour",
    "九龙": "Jiulong",
    "捷尼赛思": "Genesis",
    "景飞汽车": "Jingfei Auto",
    "骏驰": "Junchi",
    "骐蔚汽车": "Qiwei Auto",
    "极氪": "Zeekr",
    "极狐": "Arcfox",
    "极越": "Jiyue",
    "金旅": "Golden Dragon",
    "金杯": "Jinbei",
    "金琥新能源": "Jinhu NEV",
    "金龙": "King Long",
    # --- K/L ---
    "起亚": "Kia",
    "卡威": "Kawei",
    "卡文汽车": "Kawen Auto",
    "开沃汽车": "Skywell",
    "开瑞": "Kairui",
    "兰博基尼": "Lamborghini",
    "劳斯莱斯": "Rolls-Royce",
    "雷克萨斯": "Lexus",
    "LEVC": "LEVC",
    "LITE": "LITE",
    "理想": "Li Auto",
    "理想汽车": "Li Auto",
    "理念": "Everus",
    "领克": "Lynk & Co",
    "领途汽车": "Lingtu Auto",
    "林肯": "Lincoln",
    "力帆汽车": "Lifan",
    "零跑": "Leapmotor",
    "零跑汽车": "Leapmotor",
    "岚图": "Voyah",
    "岚图汽车": "Voyah",
    "蓝擎汽车": "Lanqing Auto",
    "蓝电": "Landian",
    "凌宝汽车": "Lingbao Auto",
    "灵悉": "Lingxi",
    "乐道": "Onvo",
    "路虎": "Land Rover",
    "陆地方舟": "Greenwheel",
    "Lorinser罗伦士": "Lorinser",
    "猎豹汽车": "Leopard Auto",
    "雷丁": "Levdeo",
    "雷诺": "Renault",
    "雷驰汽车": "Leichi Auto",
    # --- M ---
    "MINI": "MINI",
    "名爵": "MG",
    "马自达": "Mazda",
    "玛莎拉蒂": "Maserati",
    "迈凯伦": "McLaren",
    "迈迈": "Maimai",
    "猛士": "Mengshi",
    "摩登汽车": "Modern Auto",
    "敏安汽车": "Minan Auto",
    "未奥汽车": "Wiao Auto",
    "万象汽车": "Wanxiang Auto",
    # --- N ---
    "蔚来": "NIO",
    "哪吒": "Nezha",
    "哪吒汽车": "Nezha",
    "日产": "Nissan",
    "纳智捷": "Luxgen",
    # --- O/P ---
    "欧拉": "ORA",
    "欧铃汽车": "Ouling Auto",
    "标致": "Peugeot",
    "Polestar极星": "Polestar",
    "朋克汽车": "Punk Auto",
    # --- Q ---
    "奇瑞": "Chery",
    "奇瑞新能源": "Chery NEV",
    "奇瑞风云": "Chery Fengyun",
    "启辰": "Venucia",
    # --- R ---
    "荣威": "Roewe",
    "ROX极石": "ROX",
    "瑞驰汽车": "Ruichi Auto",
    "容大智造": "Rongda Smart",
    "睿蓝": "Ruilan",
    "睿蓝汽车": "Ruilan",
    "红星汽车": "Hongxing Auto",
    "远航": "Yuanhang",
    "远航汽车": "Yuanhang",
    "远程": "Farizon",
    "裕路": "Yulu",
    # --- S ---
    "上汽": "SAIC",
    "上汽跃进": "SAIC Yuejin",
    "SERES赛力斯": "SERES",
    "SONGSAN MOTORS": "Songsan Motors",
    "SWM斯威汽车": "SWM",
    "smart": "Smart",
    "三菱": "Mitsubishi",
    "思皓": "Sehol",
    "思铭": "Ciimo",
    "沙龙汽车": "Salon Auto",
    "申龙汽车": "Sunlong",
    "神州": "Shenzhou",
    "世极": "Shiji",
    "示界": "Shijie",
    "速达": "Suda",
    "斯达泰克": "Startech",
    "星海狮": "Xinghaishi",
    "尊界": "Zunjie",
    "尚界": "Shangjie",
    "享界": "Xiangjie",
    "智界": "Zhijie",
    "智己": "IM Motors",
    "智己汽车": "IM Motors",
    "小鹏": "XPeng",
    "小米": "Xiaomi",
    "小米汽车": "Xiaomi Auto",
    "小虎": "Xiaohu",
    # --- T ---
    "特斯拉": "Tesla",
    "腾势": "Denza",
    "坦克": "Tank",
    "天际": "Enovate",
    "天际汽车": "Enovate",
    # --- V/W ---
    "沃尔沃": "Volvo",
    "威马": "WM Motor",
    "威马汽车": "WM Motor",
    "威麟": "Weilin",
    "五菱": "Wuling",
    "五菱汽车": "Wuling Auto",
    "魏牌": "Wey",
    "潍柴英致": "Weichai Yingzhi",
    "野马汽车": "Yema",
    "野马新能源": "Yema NEV",
    # --- X ---
    "现代": "Hyundai",
    "星途": "Exeed",
    "雪佛兰": "Chevrolet",
    "雪铁龙": "Citroen",
    "新吉奥": "Xinjiao",
    "新特汽车": "Singulato",
    "新龙马汽车": "Xinlongma",
    # --- Y ---
    "仰望": "Yangwang",
    "银河": "Galaxy",
    "银隆新能源": "Yinlong NEV",
    "英菲尼迪": "Infiniti",
    "一汽": "FAW",
    "御捷": "Yujie",
    "予风汽车": "Yufeng Auto",
    "云度": "Yudo",
    "自游家": "Niutron",
    "陕汽通家": "Shaanxi Tongjia",
    # --- Z ---
    "中华": "Brilliance",
    "中国重汽": "CNHTC",
    "之诺": "Zinoro",
    "众泰": "Zotye",
    "鑫源汽车": "Xinyuan Auto",
    "几何": "Geometry",
    "埃安": "Aion",
    "埃尚": "Aishang",
    "莲花跑车": "Lotus",
    "知豆": "Zhidou",
    "菱势汽车": "Lingshi Auto",
    "依维柯": "Iveco",
    "汉腾汽车": "Hanteng Auto",
    "橙仕": "Chengshi",
    "恒天": "Hengtian",
    "中华": "Brilliance",
}


# ============================================================
# 品牌名自动英文提取 fallback
# ============================================================
def extract_english_part(cn_name):
    """从品牌名中提取英文部分作为 fallback"""
    en_parts = re.findall(r'[A-Za-z][A-Za-z0-9]*', cn_name)
    if en_parts:
        return " ".join(en_parts)
    return cn_name  # 无法提取则返回原名

def get_brand_en(cn_name):
    """获取品牌英文名"""
    if cn_name in BRAND_EN_MAP:
        return BRAND_EN_MAP[cn_name]
    return extract_english_part(cn_name)


# ============================================================
# 车系名翻译（model name）
# ============================================================
MODEL_KEYWORD_MAP = [
    # 顺序很重要：长词优先
    ("新能源", " NEV"), ("纯电动", " BEV"), ("插电混动", " PHEV"),
    ("(进口)", " Import"), ("（进口）", " Import"),
    ("电动", " EV"), ("混动", " Hybrid"),
    # 品牌前缀（去掉品牌名，保留车型名）
    ("五菱荣光小卡专用车", "Rongguang Pickup Special"),
    ("五菱扬光电卡", "Yangguang E-Truck"),
    ("五菱电卡", "E-Truck"),
    ("五菱缤果", "Bingo"), ("五菱星光", "Starlight"),
    ("五菱扬光", "Yangguang"), ("五菱", ""),
    ("宝骏云朵", "Yunduo"), ("宝骏享境", "Xiangjing"),
    ("宝骏云海", "Yunhai"), ("宝骏悦也", "Yuye"), ("宝骏", ""),
    ("欧拉闪电猫", "Lightning Cat"), ("欧拉好猫", "Good Cat"),
    ("欧拉芭蕾猫", "Ballet Cat"), ("欧拉白猫", "White Cat"),
    ("欧拉黑猫", "Black Cat"), ("欧拉", ""),
    ("岚图梦想家", "Dreamer"), ("岚图泰山", "Taishan"),
    ("岚图追光", "Chasing Light"), ("岚图知音", "Zhiyin"), ("岚图", ""),
    ("魏牌 蓝山", "Blue Mountain"), ("魏牌 高山", "Alpine"), ("魏牌", ""),
    ("哈弗枭龙", "Xiaolong"), ("哈弗", ""),
    ("吉利雷达地平线", "Radar Horizon"), ("吉利雷达金刚", "Radar Vajra"),
    ("吉利幸福号", "Fortune"),
    ("奇瑞舒享家", "Comfort Home"), ("奇瑞风云", "Fengyun"), ("奇瑞", ""),
    ("奔腾小马", "Pony"), ("奔腾", ""),
    ("睿蓝蓝气球", "Blue Balloon"), ("睿蓝", ""),
    ("北汽小河马", "Little Hippo"), ("北汽小猫", "Little Cat"), ("北汽", ""),
    ("思皓爱跑", "iPao"), ("思皓", ""),
    ("知豆彩虹", "Rainbow"), ("知豆", "Zhidou"),
    ("远程锋锐", "Fengrui"), ("远程", ""),
    ("银隆艾菲", "Effie"), ("银隆", ""),
    ("长安猎手", "Hunter"), ("长安", ""),
    ("钇为花仙子", "Fairy"),
    ("百智大熊", "Big Bear"),
    ("朋克多多", "Duoduo"), ("朋克美美", "Meimei"),
    ("陆地方舟风尚", "Fashion"),
    ("雷丁芒果", "Mango"), ("雷丁", ""),
    ("福特智趣烈马", "Smart Bronco"), ("福特电马", "Mustang Mach-E"), ("福特", ""),
    ("江淮卡拉", "Kala"), ("江淮", ""),
    ("骐蔚熊猫宏运", "Panda Hongyun"), ("骐蔚熊猫宏图", "Panda Hongtu"),
    ("菱势电卡", "E-Truck"), ("菱势黄金大卡", "Gold Truck L"),
    ("菱势黄金小卡", "Gold Truck S"), ("菱势黄金卡", "Gold Truck"),
    ("菱势黄金仓", "Gold Van"), ("菱势", ""),
    ("多拉大面", "Dora Van"),
    ("比克兴熠", "Xingyi"),
    ("安凯快乐运", "Happy Express"),
    ("凯翼拾月", "October"), ("凯翼", ""),
    ("克蒂昆仑", "Kunlun"),
    ("航天金龙", "Space Dragon"),
    ("吉奥睿征", "Ruizheng"), ("吉奥奥腾", "Aoteng"),
    ("吉奥帅凌", "Shuailing"), ("吉奥帅豹", "Shuaibao"),
    ("吉奥帅舰", "Shuaijian"), ("吉奥", ""),
    # 国际品牌车名
    ("指挥官", "Commander"), ("牧马人", "Wrangler"),
    ("大切诺基", "Grand Cherokee"), ("自由光", "Cherokee"),
    ("途观", "Tiguan"), ("途岳", "Tharu"), ("帕萨特", "Passat"),
    ("朗逸", "Lavida"), ("宝来", "Bora"), ("迈腾", "Magotan"),
    ("卡罗拉", "Corolla"), ("凯美瑞", "Camry"), ("汉兰达", "Highlander"),
    ("雅阁", "Accord"), ("思域", "Civic"), ("皓影", "Breeze"),
    ("天籁", "Altima"), ("轩逸", "Sylphy"), ("奇骏", "X-Trail"),
    ("缤越", "Binyue"), ("博越", "Boyue"), ("帝豪", "Emgrand"),
    ("星瑞", "Xingrui"), ("星越", "Xingyue"),
    ("考拉", "Kaola"), ("阿尔法", "Alpha"),
    ("探险者", "Explorer"), ("锐界", "Edge"), ("蒙迪欧", "Mondeo"),
    ("科沃兹", "Cavalier"), ("迈锐宝", "Malibu"),
    ("昂科威", "Envision"), ("君威", "Regal"), ("微蓝", "Velite"),
    ("添越", "Bentayga"), ("飞驰", "Flying Spur"),
    ("畅巡", "Menlo"),
    # 比亚迪车系
    ("宋", "Song"), ("秦", "Qin"), ("汉", "Han"), ("唐", "Tang"),
    ("元", "Yuan"), ("夏", "Xia"), ("海鸥", "Seagull"), ("海豹", "Seal"),
    ("海豚", "Dolphin"), ("驱逐舰", "Destroyer"),
    ("仰望", "Yangwang"), ("方程豹", "Leopard"),
    # 智选车品牌
    ("问界", "Wenjie"), ("智界", "Zhijie"), ("享界", "Xiangjie"),
    ("尊界", "Zunjie"), ("尚界", "Shangjie"), ("示界", "Shijie"),
    ("极狐", "ARCFOX"), ("极氪", "Zeekr"),
    # 其他常见中文车名
    ("闪灵", "Spectre"), ("星愿", "Star Wish"), ("熊猫", "Panda"),
    ("风行雷霆", "Thunder"), ("世极", "Shiji"),
    ("芝麻", "Sesame"), ("意路达", "Yiluda"),
    ("别克至境世家", "GL8 Legacy"),
    ("晨风", "Morning Wind"), ("家宝", "Jiabao"),
    ("欧麦加", "Omega"), ("乐迪", "Ledi"), ("乐福", "Lefu"),
    ("小蚂蚁", "Little Ant"), ("大蚂蚁", "Big Ant"), ("多米", "Domi"),
    ("悦虎", "Yuehu"), ("迈乔", "Maiqiao"),
    ("绎乐", "Yile"), ("江豚", "Porpoise"),
    ("花仙子", "Fairy"), ("爱跑", "iPao"),
    ("机甲龙", "Mecha Dragon"), ("快运王", "Express King"),
    ("骆驼微卡", "Camel Micro Truck"), ("骆驼", "Camel"),
    ("缤纷", "Binfun"), ("好运", "Fortune"), ("豪运", "Deluxe"),
    ("启运", "Qiyun"), ("锐捷", "Ruijie"),
    ("蓝猫", "Blue Cat"), ("钱多多", "Qianduoduo"),
    ("予风黄金仓", "Golden Van"),
    ("云兔", "Cloud Rabbit"), ("迈迈", "Maimai"),
    ("腾势", "Denza"), ("标致", ""),
    ("埃尚", "Aishang"), ("羿", "Yi"),
    ("小米", ""),
]

def translate_model_name(cn_name):
    """将中文车系名翻译为英文"""
    # 先检查是否已经是纯英文/数字
    if re.match(r'^[A-Za-z0-9\s\-\.]+$', cn_name.strip()):
        return cn_name.strip()

    result = cn_name
    # 关键词替换
    for cn, en in MODEL_KEYWORD_MAP:
        result = result.replace(cn, en)

    # 去掉剩余的中文字符，保留英文/数字/空格/连字符
    cleaned = re.sub(r'[\u4e00-\u9fff]+', ' ', result)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    # 去除开头/结尾的多余空格和符号
    cleaned = re.sub(r'^[\s\-·]+|[\s\-·]+$', '', cleaned)

    if not cleaned or cleaned == cn_name:
        # 如果翻译后为空或未变化，保留原始英文/数字部分
        en_parts = re.findall(r'[A-Za-z0-9]+', cn_name)
        return " ".join(en_parts) if en_parts else cn_name

    return cleaned



# ============================================================
# 配置名翻译（spec/variant name）
# ============================================================
SPEC_KEYWORD_MAP = [
    # 年款 — 去掉"款"字
    ("款", " "),
    # 动力类型 (长词优先)
    ("增程式", "EREV"), ("增程版", "EREV"), ("增程", "EREV"),
    ("纯电动", "BEV"), ("纯电版", "BEV"), ("纯电", "BEV"),
    ("插电混动", "PHEV"), ("插混", "PHEV"), ("混动", "Hybrid"),
    # 驱动方式
    ("后驱版", "RWD"), ("后驱", "RWD"),
    ("前驱版", "FWD"), ("前驱", "FWD"),
    ("四驱版", "AWD"), ("四驱", "AWD"),
    ("两驱版", "2WD"), ("两驱", "2WD"),
    ("单电机", "Single Motor"), ("双电机", "Dual Motor"),
    # 续航
    ("超长续航版", "Max Range"), ("超长续航", "Max Range"),
    ("长续航版", "Long Range"), ("长续航", "Long Range"),
    ("标准续航版", "Standard Range"), ("标准续航", "Standard Range"),
    # 配置级别
    ("旗舰版", "Flagship"), ("旗舰型", "Flagship"), ("旗舰", "Flagship"),
    ("尊贵版", "Premium"), ("尊贵型", "Premium"), ("尊贵", "Premium"),
    ("豪华版", "Luxury"), ("豪华型", "Luxury"), ("豪华", "Luxury"),
    ("舒适版", "Comfort"), ("舒适型", "Comfort"), ("舒适", "Comfort"),
    ("精英版", "Elite"), ("精英型", "Elite"), ("精英", "Elite"),
    ("领先版", "Leading"), ("领先型", "Leading"), ("领先", "Leading"),
    ("标准版", "Standard"), ("标准型", "Standard"),
    ("运动版", "Sport"), ("运动型", "Sport"), ("运动", "Sport"),
    ("畅行版", "Comfort"), ("畅行型", "Comfort"), ("畅行", "Comfort"),
    ("创领版", "Pioneer"), ("创领型", "Pioneer"),
    ("智享版", "Smart"), ("智享型", "Smart"), ("智享", "Smart"),
    ("悦享版", "Joy"), ("悦享型", "Joy"), ("悦享", "Joy"),
    ("进取版", "Active"), ("进取型", "Active"), ("进取", "Active"),
    ("时尚版", "Fashion"), ("时尚型", "Fashion"),
    ("科技版", "Tech"), ("科技型", "Tech"),
    ("出行版", "Travel"), ("出行型", "Travel"),
    ("基本型", "Base"), ("基本版", "Base"),
    ("家庭版", "Family"), ("家庭型", "Family"),
    # 座位
    ("7座版", "7-Seat"), ("7座", "7-Seat"),
    ("6座版", "6-Seat"), ("6座", "6-Seat"),
    ("5座版", "5-Seat"), ("5座", "5-Seat"),
    ("4座版", "4-Seat"), ("4座", "4-Seat"),
    # 其他
    ("改款", "Facelift"),
    ("限定版", "Limited"), ("限量版", "Limited"),
    ("定制版", "Custom"),
    ("创始版", "Founder"), ("创始人版", "Founder"),
    ("冠军版", "Champion"),
    ("荣耀版", "Glory"), ("荣耀", "Glory"),
    ("星耀版", "Star"), ("星耀", "Star"),
    ("城市版", "City"),
    ("越野版", "Offroad"),
    ("行政版", "Executive"),
    ("尊享版", "Exclusive"), ("尊享型", "Exclusive"),
    ("臻享版", "Premium+"),
    ("高性能版", "Performance"), ("性能版", "Performance"),
    ("入门版", "Entry"),
    ("版", ""),
    ("型", ""),
]

def translate_spec_name(cn_spec):
    """将中文配置名翻译为英文"""
    if re.match(r'^[A-Za-z0-9\s\-\.]+$', cn_spec.strip()):
        return cn_spec.strip()

    result = cn_spec
    for cn, en in SPEC_KEYWORD_MAP:
        result = result.replace(cn, en)

    # 去掉剩余中文字符
    cleaned = re.sub(r'[\u4e00-\u9fff]+', ' ', result)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    if not cleaned:
        en_parts = re.findall(r'[A-Za-z0-9]+', cn_spec)
        return " ".join(en_parts) if en_parts else cn_spec

    return cleaned


# ============================================================
# 主处理流程
# ============================================================
def main():
    print("=" * 60)
    print("  品牌/车系/配置名称英文化处理")
    print("=" * 60)

    # 读取 brands.json
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    brands = data.get("brands", [])
    print(f"\n  读取到 {len(brands)} 个品牌")

    stats = {"brand_translated": 0, "model_translated": 0, "spec_translated": 0}

    for brand in brands:
        # 翻译品牌名
        old_en = brand.get("nameEn", brand["name"])
        new_en = get_brand_en(brand["name"])
        brand["nameEn"] = new_en
        if new_en != old_en:
            stats["brand_translated"] += 1

        # 翻译每个车系
        for model in brand.get("models", []):
            model_en = translate_model_name(model["name"])
            model["nameEn"] = model_en
            stats["model_translated"] += 1

            # 翻译每个配置
            for variant in model.get("variants", []):
                spec_en = translate_spec_name(variant["specName"])
                variant["specNameEn"] = spec_en
                stats["spec_translated"] += 1

    # 写回 JSON
    with open(INPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n  品牌名更新: {stats['brand_translated']} 个")
    print(f"  车系名翻译: {stats['model_translated']} 个")
    print(f"  配置名翻译: {stats['spec_translated']} 个")
    print(f"\n  数据已写回: {INPUT_PATH}")
    print("=" * 60)

    # 打印前5个品牌的翻译结果作为预览
    print("\n=== 翻译结果预览（前5个品牌）===")
    for brand in brands[:5]:
        print(f"\n  {brand['name']} -> {brand['nameEn']}")
        for model in brand.get("models", [])[:3]:
            print(f"    {model['name']} -> {model.get('nameEn', '?')}")
            for v in model.get("variants", [])[:2]:
                print(f"      {v['specName']} -> {v.get('specNameEn', '?')}")


if __name__ == "__main__":
    main()