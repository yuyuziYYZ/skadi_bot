import json
from urllib.parse import urlsplit
from requests_html import HTMLSession
import requests
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.typing import T_State
from nonebot.plugin import on_command

# 获取图片
def get_setu():
    url='https://api.iyk0.com/ecy/api.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c


st = on_keyword(keywords={'蒂蒂涩图','蒂蒂setu','蒂蒂色图','蒂蒂每日一图'}, priority=2,block=True)
@st.handle()
async def st_(bot: Bot, event: Event):
    try:
        url=str(get_setu())
        if int(event.get_user_id()) != event.self_id:
            await st.send(MessageSegment.image(file=str(url)))
    except Exception as e:
        await st.send("涩图出现故障")