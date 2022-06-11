import nonebot
from nonebot import on_command, logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.adapters.onebot.v11.exception import ActionFailed
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER
from .utils import At, banSb, init
from .config import plugin_config

cb_notice = plugin_config.callback_notice

admin_init =  on_command('群管初始化', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)


@admin_init.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    await init()

ban = on_command('禁', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)


@ban.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /禁 @user 禁言
    """
    msg = str(event.get_message()).replace(" ", "").split("]")
    sb = At(event.json())
    gid = event.group_id
    if sb:
        if len(msg) > len(sb) and msg[-1] != "":
            try:
                time = int(msg[-1:][0])
            except ValueError:
                for q in sb:
                    raw_msg = event.raw_message.replace(" ", "").replace(str(q), "")
                time = int(''.join(str(num) for num in list(filter(lambda x: x.isdigit(), raw_msg))))
            baning = banSb(gid, ban_list=sb, time=time)
            async for baned in baning:
                if baned:
                    try:
                        await baned
                    except ActionFailed:
                        await ban.finish("权限不足")
                    else:
                        logger.info("禁言操作成功")
                        if cb_notice:
                            await ban.finish("禁言操作成功")
        else:
            baning = banSb(gid, ban_list=sb)
            async for baned in baning:
                if baned:
                    try:
                        await baned
                    except ActionFailed:
                        await ban.finish("权限不足")
                    else:
                        logger.info("禁言操作成功")
                        if cb_notice:
                            await ban.finish("禁言操作成功")
                await ban.send(f"该用户已被禁言随机时长")


unban = on_command("解", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER)


@unban.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /解 @user 解禁
    """
    msg = str(event.get_message())
    sb = At(event.json())
    gid = event.group_id
    if sb:
        # if len(msg.split()) == len(sb):
        baning = banSb(gid, ban_list=sb, time=0)
        async for baned in baning:
            if baned:
                try:
                    await baned
                except ActionFailed:
                    await unban.finish("权限不足")
                else:
                    logger.info("解禁操作成功")
                    if cb_notice:
                        await unban.finish("解禁操作成功")


ban_all = on_command("all", permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@ban_all.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /all 全员禁言
    /all  解 关闭全员禁言
    """
    msg = event.get_message()
    if msg and '解' in str(msg):
        enable = False
    else:
        enable = True
    try:
        await bot.set_group_whole_ban(
            group_id=event.group_id,
            enable=enable
        )
    except ActionFailed:
        await ban_all.finish("权限不足")
    else:
        logger.info(f"全体操作成功 {str(enable)}")
        if cb_notice:
            await ban_all.finish(f"全体操作成功 {str(enable)}")


change = on_command('改', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@change.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /改 @user xxx 改群昵称
    """
    msg = str(event.get_message())
    logger.info(msg.split())
    sb = At(event.json())
    gid = event.group_id
    if sb:
        try:
            for user_ in sb:
                await bot.set_group_card(
                    group_id=gid,
                    user_id=int(user_),
                    card=msg.split()[-1:][0]
                )
        except ActionFailed:
            await change.finish("权限不足")
        else:
            logger.info("改名片操作成功")
            if cb_notice:
                await change.finish("改名片操作成功")


title = on_command('头衔', permission=SUPERUSER | GROUP_OWNER, priority=1, block=True)


@title.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /头衔 @user  xxx  给某人头衔
    """
    msg = str(event.get_message())
    stitle = msg.split()[-1:][0]
    logger.info(str(msg.split()), stitle)
    sb = At(event.json())
    gid = event.group_id
    if sb:
        if 'all' not in sb:
            try:
                for qq in sb:
                    await bot.set_group_special_title(
                        group_id=gid,
                        user_id=int(qq),
                        special_title=stitle,
                        duration=-1,
                    )
            except ActionFailed:
                await title.finish("权限不足")
            else:
                logger.info(f"改头衔操作成功{stitle}")
                if cb_notice:
                    await title.finish(f"改头衔操作成功{stitle}")
        else:
            await title.finish("未填写头衔名称 或 不能含有@全体成员")


title_ = on_command('删头衔', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@title_.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /删头衔 @user 删除头衔
    """
    msg = str(event.get_message())
    stitle = msg.split()[-1:][0]
    logger.info(str(msg.split()), stitle)
    sb = At(event.json())
    gid = event.group_id
    if sb:
        if 'all' not in sb:
            try:
                for qq in sb:
                    await bot.set_group_special_title(
                        group_id=gid,
                        user_id=int(qq),
                        special_title="",
                        duration=-1,
                    )
            except ActionFailed:
                await title_.finish("权限不足")
            else:
                logger.info(f"改头衔操作成功{stitle}")
                if cb_notice:
                    await title_.finish(f"改头衔操作成功{stitle}")


kick = on_command('踢', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@kick.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    /踢 @user 踢出某人
    """
    msg = str(event.get_message())
    sb = At(event.json())
    gid = event.group_id
    if sb:
        if 'all' not in sb:
            try:
                for qq in sb:
                    await bot.set_group_kick(
                        group_id=gid,
                        user_id=int(qq),
                        reject_add_request=False
                    )
            except ActionFailed:
                await kick.finish("权限不足")
            else:
                logger.info(f"踢人操作成功")
                if cb_notice:
                    await kick.finish(f"踢人操作成功")
        else:
            await kick.finish("不能含有@全体成员")


kick_ = on_command('黑', permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=1, block=True)


@kick_.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    黑 @user 踢出并拉黑某人
    """
    msg = str(event.get_message())
    sb = At(event.json())
    gid = event.group_id
    if sb:
        if 'all' not in sb:
            try:
                for qq in sb:
                    await bot.set_group_kick(
                        group_id=gid,
                        user_id=int(qq),
                        reject_add_request=True
                    )
            except ActionFailed:
                await kick_.finish("权限不足")
            else:
                logger.info(f"踢人并拉黑操作成功")
                if cb_notice:
                    await kick_.finish(f"踢人并拉黑操作成功")
        else:
            await kick_.finish("不能含有@全体成员")


set_g_admin = on_command("管理员+", permission=SUPERUSER | GROUP_OWNER, priority=1, block=True)


@set_g_admin.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    管理员+ @user 添加群管理员
    """
    msg = str(event.get_message())
    logger.info(msg)
    logger.info(msg.split())
    sb = At(event.json())
    logger.info(sb)
    gid = event.group_id
    if sb:
        if 'all' not in sb:
            try:
                for qq in sb:
                    await bot.set_group_admin(
                        group_id=gid,
                        user_id=int(qq),
                        enable=True
                    )
            except ActionFailed:
                await set_g_admin.finish("权限不足")
            else:
                logger.info(f"设置管理员操作成功")
                await set_g_admin.finish("设置管理员操作成功")
        else:
            await set_g_admin.finish("指令不正确 或 不能含有@全体成员")

unset_g_admin = on_command("管理员-", permission=SUPERUSER | GROUP_OWNER, priority=1, block=True)


@unset_g_admin.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    管理员+ @user 添加群管理员
    """
    msg = str(event.get_message())
    logger.info(msg)
    logger.info(msg.split())
    sb = At(event.json())
    logger.info(sb)
    gid = event.group_id
    if sb:
        if 'all' not in sb:
            try:
                for qq in sb:
                    await bot.set_group_admin(
                        group_id=gid,
                        user_id=int(qq),
                        enable=False
                    )
            except ActionFailed:
                await unset_g_admin.finish("权限不足")
            else:
                logger.info(f"取消管理员操作成功")
                await unset_g_admin.finish("取消管理员操作成功")
        else:
            await unset_g_admin.finish("指令不正确 或 不能含有@全体成员")