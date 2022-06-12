# -*- coding: utf-8 -*-

import os
import json
import random



"""
明日方舟抽卡系统
输入指令 draw
输出抽卡结果 str
    干员名字+职业+星星数量
    干员名字+职业+星星数量

逻辑
设置抽卡次数，读取卡池
每次抽卡进行概率判定，随即从卡池获得干员并储存在list中
最后输出抽到的干员
"""
# 简单数据库
# 基本常量
START_ADD = 50  # 保底数量(修改为0时无保底)
RATIO_PER_ADD = 2  # 保底后每次概率增加
RATIO_6_STARS = 2  # 六星概率
RATIO_5_STARS = 8  # 五星概率
RATIO_4_STARS = 50  # 四星概率

# Up池子设置
chance_up = [[], [], ['濯尘芙蓉', '蓝毒'], ['黑键']]  # 特殊UP活动,分别对应3、4、5、6

# 统计数据变量
operator_list = [[], [], [], []]  # 干员列表
operator_names = [[], [], [], []]  # 干员名字
list_count = [[], [], [], []]  # 抽取数量统计
total_count = 0  # 总抽取数量
save_count = 0  # 保底统计


async def arknights_gacha(roll_times):
    # 读取数据初始化
    gacha_init()
    # 随机抽卡过程
    """
    生成随机概率，与默认概率比较，获得单次抽取对应的干员
    """
    gachaList = gacha_get_list(roll_times)
    result_list = generate_data(gachaList)
    return result_list


def gacha_init():
    global operator_list, list_count
    with open(os.path.abspath('./src/plugins/arknights_gacha/constData') + '/character_table.json', 'r',encoding='utf-8') as infile:
        js = json.loads(infile.read())
        for (key, value) in js.items():
            rarity = value["rarity"]
            if rarity > 1:
                if key.startswith('token'):  # 前缀检测，防止召唤物导致结果异常
                    continue
                if key.endswith('robin') or key.endswith('amiya') or key.endswith('rosmon') \
                        or key.endswith('sophia') or key.endswith('mint') or key.endswith('amedic') \
                        or key.endswith('acast') or key.endswith('aguard') or key.endswith('asnipe') \
                        or key.endswith('rsnipe') or key.endswith('rcast') or key.endswith('rmedic') \
                        or key.endswith('rguard') or key.endswith('folivo') or key.endswith('folnic') \
                        or key.endswith('cqbw') or key.endswith('nian') or key.endswith('tiger') \
                        or key.endswith('hpsts') or key.endswith('savage') or key.endswith('grani') \
                        or key.endswith('flameb') or key.endswith('ceylon') or key.endswith('bison') \
                        or key.endswith('durnar') or key.endswith('ccheal') or key.endswith('blackd') \
                        or key.endswith('ethan') or key.endswith('estell') \
                        or key.endswith('breeze') or key.endswith('snsant') or key.endswith('finlpp'):  # 后缀检测，去除公招限定
                    continue
                operator_list[rarity - 2].append(key)
                operator_names[rarity - 2].append(value['name'])
                list_count[rarity - 2].append(0)


# 获得一个抽卡干员
def get_gacha_item(rarity):
    l1 = len(operator_names[rarity - 3])
    l2 = len(chance_up[rarity - 3])
    if l2 != 0:
        if rarity == 3:
            if random.randrange(1, 6) == 1:
                return chance_up[rarity - 3][random.randrange(0, l2)]
        if random.randrange(1, 3) == 1:
            return chance_up[rarity - 3][random.randrange(0, l2)]
    return operator_names[rarity - 3][random.randrange(0, l1)]


# 计算保底概率
def get_save_chance():
    ratio_save = RATIO_6_STARS
    # 判断是否有保底
    if START_ADD == 0:
        return ratio_save
    # 保底计算
    if save_count > START_ADD:
        ratio_save += (save_count - START_ADD) * RATIO_PER_ADD
    return ratio_save


# 抽卡判定
def gacha_get_list(roll_times):
    global total_count, save_count
    gachaList = [[], []]
    for i in range(roll_times):
        s = random.randrange(1, 101)
        # 获得六星保底的概率数据
        chance = get_save_chance()
        if s <= chance:
            total_count += 1
            save_count = 0
            gachaList[0].append("★★★★★★")
            gachaList[1].append(get_gacha_item(6))
        elif s <= chance + RATIO_5_STARS:
            total_count += 1
            save_count += 1
            gachaList[0].append("★★★★★  ")
            gachaList[1].append(get_gacha_item(5))
        elif s <= chance + RATIO_5_STARS + RATIO_4_STARS:
            total_count += 1
            save_count += 1
            gachaList[0].append("☆☆☆☆    ")
            gachaList[1].append(get_gacha_item(4))
        else:
            total_count += 1
            save_count += 1
            gachaList[0].append("☆☆☆      ")
            gachaList[1].append(get_gacha_item(3))
    return gachaList

# 生成结果字符串
def generate_data(gachaList: list):
    str = ""
    for i in range(len(gachaList[0])):
        str += gachaList[0][i] + " " + gachaList[1][i] + "\n"
    return str


# if __name__ == "__main__":
#     arknights_gacha(10)
