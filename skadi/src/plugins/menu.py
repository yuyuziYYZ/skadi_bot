from email.mime import image
from importlib.resources import path
from pathlib import Path

from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command

local_menu = on_command("菜单")


@local_menu.handle()
async def handle_local_menu():
    # 本地图片位置
    path = Path(__file__).parent / "menu.png"
    # 构造图片消息段
    image = MessageSegment.image(path)
    # 发送图片
    await local_menu.finish(image)

ark_menu = on_command("方舟菜单",aliases={"方舟menu"})


@ark_menu.handle()
async def handle_local_menu():
    # 本地图片位置
    path = Path(__file__).parent / "ark_menu.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    # 发送图片
    await ark_menu.finish(image)



admin_menu = on_command("群管", aliases={"群管菜单"})

@admin_menu.handle()
async def handle_setu_menu():
    #本地图片位置
    path = Path(__file__).parent / "admin.jpg"
    #构造图片信息段
    image = MessageSegment.image(path)
    #发送图片
    await admin_menu.finish(image)


horse_menu = on_command("赛马", aliases={"赛马菜单"})

@horse_menu.handle()
async def handle_setu_menu():
    #本地图片位置
    path = Path(__file__).parent / "horse_race.jpg"
    #构造图片信息段
    image = MessageSegment.image(path)
    #发送图片
    await horse_menu.finish(image)

