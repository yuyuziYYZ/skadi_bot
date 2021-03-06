from nonebot import on_command
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.typing import T_State

from ...database import DB as db
from ...utils import get_type_id, permission_check, to_me, handle_uid


live_on = on_command("开启直播", priority=5)
live_on.__doc__ = """开启直播 UID"""

live_on.handle()(permission_check)

live_on.handle()(handle_uid)


@live_on.got("uid", prompt="请输入要开启直播的UID")
async def _(event: MessageEvent, state: T_State):
    """根据 UID 开启直播"""

    if await db.set_sub(
        "live",
        True,
        uid=state["uid"],
        type=event.message_type,
        type_id=get_type_id(event),
    ):
        user = await db.get_user(uid=state["uid"])
        assert user is not None
        await live_on.finish(f"已开启 {user.name}（{user.uid}）的直播推送")
    await live_on.finish(f"UID（{state['uid']}）未关注，请先关注后再操作")
