from email.mime import image
from importlib.resources import path
from pathlib import Path

from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command

setu_menu = on_command("涩图菜单")

@setu_menu.handle()
async def handle_setu_menu():
    #本地图片位置
    path = Path(__file__).parent / "setumenu.jpg"
    #构造图片信息段
    image = MessageSegment.image(path)
    #发送图片
    await setu_menu.finish(image)