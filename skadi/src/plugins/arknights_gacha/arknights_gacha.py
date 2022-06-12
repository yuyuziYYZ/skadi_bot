# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from .gacha import *
from nonebot.typing import T_State

arknights = on_command("十连", priority=1)
# regex(r"\d{1,2}$")

@arknights.handle()
async def handle_roll_times(bot: Bot, event: GroupMessageEvent, state: T_State):
    state["roll_times"] = 10
    roll_times = state["roll_times"]

    result_list = await arknights_gacha(int(roll_times))
    await arknights.send(
        message="\n" + result_list,
        at_sender=True)