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

def get_tuizi():
    url='https://api.ghser.com/random/api.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c

sese = on_keyword(keywords={'蒂蒂涩涩','蒂蒂色色'}, priority=2,block=True)
@sese.handle()
async def st_(bot: Bot, event: Event):
    try:
        url=str(get_tuizi())
        if int(event.get_user_id()) != event.self_id:
            await sese.send(MessageSegment.image(file=str(url)))
    except Exception as e:
        await sese.send("涩涩出现故障")
