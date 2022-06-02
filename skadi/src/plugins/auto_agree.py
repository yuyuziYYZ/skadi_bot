from nonebot import on_request
from nonebot.adapters.onebot.v11 import Bot, FriendRequestEvent, GroupRequestEvent


friend_req = on_request(priority=5)


@friend_req.handle()
async def friend_agree(bot: Bot, event: FriendRequestEvent):
    await bot.set_friend_add_request(flag=event.flag, approve=True)


group_add = on_request(priority=5)


@group_add.handle()
async def group_agree(bot: Bot, event: GroupRequestEvent):
    await bot.set_group_add_request(flag=event.flag, sub_type="add", approve=True)


group_invite = on_request(priority=5)


@group_invite.handle()
async def group_gree(bot:Bot, event: GroupRequestEvent):
    await bot.set_group_add_request(flag=event.flag, sub_type="invite", approve=True)