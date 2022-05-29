from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot,FriendAddNoticeEvent,GroupRequestEvent

add_friend=on_notice()
@add_friend.handle()
async def ad_f(bot:Bot,event:FriendAddNoticeEvent,state:T_State):
    await bot.call_api("set_friend_add_request",**{})#全部同意

add_group=on_notice()
@add_group.handle()
async def ad_g(bot:Bot,event:GroupRequestEvent,state:T_State):
    flag=event.flag
    sub_type=event.sub_type
    await bot.call_api("set_group_add_request",**{
        'flag':flag,
        'sub_type':sub_type,
        'approve':True
    })