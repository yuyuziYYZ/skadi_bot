from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER
from nonebot.params import State
from nonebot.permission import SUPERUSER

dismiss = on_command(
    "dismiss",
    aliases={"退群"},
    priority=1,
    permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN,
)


@dismiss.handle()
async def d1(bot: Bot, event: GroupMessageEvent, state: dict = State()):
    await bot.set_group_leave(group_id=event.group_id)