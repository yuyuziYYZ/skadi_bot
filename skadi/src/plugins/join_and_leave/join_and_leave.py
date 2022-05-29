from nonebot import on_notice
from nonebot.params import State
from nonebot.adapters.onebot.v11 import Adapter
Adapter.get_name()  # "OneBot V11"
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
import json
import os
from .config import Config


__plugin_name__ = 'join_and_leave'
__plugin_usage__ = '用法： 提示有人加群或者退群，并记录此人在该群的历史退群次数。'


img_path = 'file:///' + os.path.split(os.path.realpath(__file__))[0] + '/img/'


# 发送图片时用到的函数, 返回发送图片所用的编码字符串
def send_img(img_name):
    global img_path
    return MessageSegment.image(img_path + img_name)


# 通报加群与退群
join_and_leave = on_notice(priority=Config.priority)


@join_and_leave.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State = State()):
    try:
        ids = event.get_session_id()
    except:
        pass
    # 如果读取正常没有出错，因为有些notice格式不支持session
    else:
        # 如果这是一条群聊信息
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            # 只对列表中的群使用
            description = event.get_event_description()
            values = json.loads(description.replace("'", '"'))
            # 有新人加群
            if values['notice_type'] == 'group_increase':
                await join_and_leave.finish(
                        "欢迎刀客塔" + MessageSegment.at(values['user_id']) + '\n斯卡蒂，赏金猎人，你当真要签下我？我可是那种，会给你带来灾祸的人哦\n请发送【蒂蒂菜单】获取使用帮助\n蒂蒂大群144812758' + send_img("skadi.jpg"))
                    
            # 有人退群
            elif values['notice_type'] == 'group_decrease':                    
                # 自己退群
                if values['sub_type'] == 'leave':
                    infos = str(await bot.get_stranger_info(user_id=values['user_id']))
                    nickname = json.loads(infos.replace("'", '"'))['nickname'] + '(' + str(values['user_id']) + ')'
                    await join_and_leave.finish(
                        nickname + '快走吧，博士......逃走吧，从这里，从我身边......逃走吧。')
                # 被踢出群
                elif values['sub_type'] == 'kick':
                    infos = str(await bot.get_stranger_info(user_id=values['user_id']))
                    nickname = json.loads(infos.replace("'", '"'))['nickname'] + '(' + str(values['user_id']) + ')'
                    operator_infos = str(await bot.get_stranger_info(user_id=values['operator_id']))
                    operator_nickname = json.loads(operator_infos.replace("'", '"'))['nickname'] + '(' + str(
                        values['operator_id']) + ')'
                    await join_and_leave.finish('博士 ' + operator_nickname + ' 把' + \
                        nickname + '赶走了' + send_img("skadi.jpg"))

