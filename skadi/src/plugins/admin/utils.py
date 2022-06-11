import json
import random
import nonebot
from nonebot import logger

from .config import plugin_config, global_config
su = global_config.superusers

def At(data: str):
    """
    检测at了谁，返回[qq, qq, qq,...]
    包含全体成员直接返回['all']
    如果没有at任何人，返回[]
    :param data: event.json
    :return: list
    """
    try:
        qq_list = []
        data = json.loads(data)
        for msg in data["message"]:
            if msg["type"] == "at":
                if 'all' not in str(msg):
                    qq_list.append(int(msg["data"]["qq"]))
                else:
                    return ['all']
        return qq_list
    except KeyError:
        return []


async def init():
    """
    初始化配置文件
    :return:
    """
async def banSb(gid: int, ban_list: list, **time: int):
    """
    构造禁言
    :param gid: 群号
    :param time: 时间（s)
    :param ban_list: at列表
    :return:禁言操作
    """
    if 'all' in ban_list:
        yield nonebot.get_bot().set_group_whole_ban(
            group_id=gid,
            enable=True
        )
    else:
        if not time:
            time = random.randint(1, 600)
        else:
            time = time['time']
        for qq in ban_list:
            if int(qq) in su or str(qq) in su:
                logger.info(f"SUPERUSER无法被禁言")
            else:
                yield nonebot.get_bot().set_group_ban(
                    group_id=gid,
                    user_id=qq,
                    duration=time,
                )
