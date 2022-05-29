from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment,Event
import requests
import json
 
fy = on_keyword({'蒂蒂翻译'})
 
@fy.handle()
async def sj(bot: Bot, event: Event, state: T_State):
    anses = str(event.get_message()).strip()
    ansek = anses.strip('蒂蒂翻译')
    url = f'http://hm.suol.cc/API/fy.php?msg={ansek}'
    k = requests.get(url)
    ans = k.text
    mxy = '——Power by 语'
    ans_a = f'{ans}\n{mxy}'
    await fy.finish(Message(f'{ans_a}'))
    
    
 