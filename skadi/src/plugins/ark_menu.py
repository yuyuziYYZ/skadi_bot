from email.mime import image
from importlib.resources import path
from pathlib import Path

from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command

local_menu = on_command("方舟菜单",aliases={"方舟menu"})


@local_menu.handle()
async def handle_local_menu():
    # 本地图片位置
    path = Path(__file__).parent / "ark_menu.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    # 发送图片
    await local_menu.finish(image)

