from urllib import request


import os
from requests_html import HTMLSession
import requests
from nonebot import on_command
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
import random
from nonebot.adapters.onebot.v11 import MessageSegment
import json

def get_draw():
    url='http://api.baimianxiao.cn/arknights/arknightsdraw/main.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c

game_draw = on_command("十连寻访", priority=1,block=True)
@game_draw.handle()
async def st_(bot: Bot, event: Event):
    try:
        url=str(get_draw())
        if int(event.get_user_id()) != event.self_id:
            await game_draw.send(MessageSegment.image(file=str(url)))
    except Exception as e:
        await game_draw.send(" ")