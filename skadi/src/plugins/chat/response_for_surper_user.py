from nonebot.plugin import on_command
from nonebot import on_keyword, require
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment,Event
import requests
import json
import requests

# 用于处理超级用户信息的函数
async def get_response_for_surper_user(bot, chat, msg, user_id, group_id, default_ban_time, last_response,
                                 words, send_img, cool_down, random_response):

    
    if "我只离开了几分钟" in msg:
        return "你们就搞出这种大新闻！这像话吗？！"