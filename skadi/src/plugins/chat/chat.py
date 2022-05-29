from nonebot import on_message, on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .config import Config
from time import time
import os
from nonebot.adapters import MessageSegment
import json
from collections import Counter
from random import randint
from .response_for_surper_user import *
from .response_for_common_user import *
from .response_for_all_time import *

__plugin_name__ = 'chat'
__plugin_usage__ = '用法： 日常聊天中响应关键词与戳一戳。'

img_path = 'file:///' + os.path.split(os.path.realpath(__file__))[0] + '/img/'

# 发送图片时用到的函数, 返回发送图片所用的编码字符串
def send_img(img_name):
    global img_path
    return MessageSegment.image(img_path + img_name)


# 记录上一次响应时间
last_response = {}
last_notice_response = {}

# 初始化时间戳， 初始化为开机时间-cd时间
init_last_response = time() - Config.chat_cd
init_last_notice_response = time() - Config.notice_cd
for group_id in Config.used_in_group:
    last_response[group_id] = init_last_response
    last_notice_response[group_id] = init_last_notice_response


# 判断是否过了响应cd的函数，默认使用配置文件中的cd
# 如果已经超过了最短响应间隔，返回True
def cool_down(group_id, cd = Config.chat_cd):
    global last_response
    return time() - last_response[group_id] > cd


# 以指定概率p返回True或者False
# 用于随机决定是否要回应
# 默认值为配置文件中的默认聊天响应概率
def random_response(p = Config.p_chat_response):
    return randint(0, 99) < p


chat = on_message(priority=Config.priority)


# 针对聊天信息
@chat.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    # 上次响应时间
    global last_response
    ids = event.get_session_id()
    # 只对于群聊信息进行响应
    if ids.startswith("group"):
        # 拆解得到群号与用户号
        _, group_id, user_id = event.get_session_id().split("_")
        # 只对位于启用列表内的群组和非bot自身发送的信息进行响应
        if group_id in Config.used_in_group and user_id != Config.bot_id:
            # 获取信息文本
            msg = str(event.get_message()).strip().replace('\r\n', '').replace('\n', '').replace(' ', '')
            # 对信息内的所有文本进行出现频率统计
            words = Counter(msg)
            # 默认基础禁言时间
            default_ban_time = Config.default_ban_time

            # 1. 执行超级用户信息处理
            # 超级用户无视冷却cd，也不会重置冷却cd
            if user_id in Config.super_uid:
                response = await get_response_for_surper_user(bot, chat, msg, user_id, group_id, default_ban_time, last_response,
                                                        words, send_img, cool_down, random_response)
                # 如果回应不为空
                if response:
                    # 发送响应字符串
                    await chat.finish(response)

            # 2. 执行无冷却cd的违禁信息检查，忽略超级用户
            if user_id not in Config.super_uid:
                response = await get_response_for_all_time(bot, chat, msg, user_id, group_id, default_ban_time, last_response,
                                                        words, send_img, cool_down, random_response)
                # 如果回应不为空
                if response:
                    # 发送响应字符串
                    await chat.finish(response)

            # 3. 执行普通用户信息处理，如果超级用户的响应为空，也要进入这一步
            # 用户是否为超级用户
            is_super_user = user_id in Config.super_uid
            response = await get_response_for_common_user(bot, chat, msg, user_id, group_id, default_ban_time, last_response,
                                                        words, send_img, cool_down, random_response, is_super_user)
            # 如果回应不为空
            if response:
                # 只有普通用户信息处理需要更新最近响应时间
                if user_id not in Config.super_uid:
                    last_response[group_id] = time()
                # 发送响应字符串
                await chat.finish(response)


# --------以下信息用于对bot的戳一戳响应-------------

# 记录上一次戳机器人的nickname
last_notice_nickname = {}

# 记录cd内再次戳之后的吐槽次数
response = 0

# poke_ban_list[群组id][QQ号]得到被封禁次数
# 每次禁言默认事件*2^已经被封禁次数
poke_ban_list = {}
# 初始化
for group_id in Config.used_in_group:
    poke_ban_list[group_id] = {}

# 针对戳一戳
chat_notice = on_notice(priority=Config.priority)


@chat_notice.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    global last_notice_response
    global last_notice_nickname
    global response
    try:
        ids = event.get_session_id()
    except:
        pass
    # 如果读取正常没有出错，因为有些notice格式不支持session
    else:
        # 如果这是一条群聊信息
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            # 只对列表中的群使用
            if group_id in Config.used_in_group:
                description = event.get_event_description()
                values = json.loads(description.replace("'", '"'))
                # 如果被戳的是机器人
                if values['notice_type'] == 'notify' and values['sub_type'] == 'poke' and str(
                        values['target_id']) == Config.bot_id:
                    if user_id in Config.super_uid:
                        await chat_notice.finish("我爱你，博士")
                    # 如果不在响应cd
                    elif time() - last_notice_response[group_id] >= Config.notice_cd:
                        if randint(0, 99) < Config.p_poke_response:
                            last_notice_response[group_id] = time()
                            infos = str(await bot.get_stranger_info(user_id=values['user_id']))
                            nickname = json.loads(infos.replace("'", '"'))['nickname'] + '(' + str(
                                values['user_id']) + ')'
                            last_notice_nickname[group_id] = nickname
                            response = 0
                            # 清空ban列表
                            poke_ban_list[group_id] == {}
                            await chat_notice.finish(
                                nickname + "我爱你，博士")
                    else:
                        if response == 0:
                            if randint(0, 99) < Config.p_poke_response:
                                response += 1
                                poke_ban_list[group_id][user_id] = 1
                                await chat_notice.finish(
                                    "不要再戳啦！")
                        elif response == 1:
                            if randint(0, 99) < Config.p_poke_response:
                                response += 1
                                if user_id in poke_ban_list[group_id]:
                                    poke_ban_list[group_id][user_id] += 1
                                else:
                                    poke_ban_list[group_id][user_id] = 1
                                await chat_notice.finish(
                                    "呀！再这样就不理你们了！")
                        elif response == 2:
                            if randint(0, 99) < Config.p_poke_response:
                                response += 1
                                # 如果戳过了，那么每戳一次就把禁言时间翻倍
                                if user_id in poke_ban_list[group_id]:
                                    poke_ban_list[group_id][user_id] += 1
                                else:
                                    poke_ban_list[group_id][user_id] = 1
                                try:
                                    await bot.set_group_ban(group_id=group_id, user_id=user_id,
                                                            duration=Config.default_ban_time * (
                                                                        2 ** (poke_ban_list[group_id][user_id] - 1)))
                                except:
                                    pass
                                await chat_notice.finish("刀客塔！再戳我就生气了！")
                        else:
                            # 如果戳过了，那么每戳一次就把禁言时间翻倍
                            if user_id in poke_ban_list[group_id]:
                                poke_ban_list[group_id][user_id] += 1
                            else:
                                poke_ban_list[group_id][user_id] = 1
                            try:
                                await bot.set_group_ban(group_id=group_id, user_id=user_id,
                                                        duration=Config.default_ban_time * (
                                                                    2 ** (poke_ban_list[group_id][user_id] - 1)))
                            except:
                                pass

