from random import choice
import asyncio
import re
from unicodedata import name

# 用于处理普通用户信息的函数
async def get_response_for_common_user(bot, chat, msg, user_id, group_id, default_ban_time, last_response,
                                 words, send_img, cool_down, random_response, is_super_user):
    # 使用默认冷却cd与默认概率的响应
    if (cool_down(group_id) and random_response()) or is_super_user:                     
        # 随机返回响应
        if "抱蒂蒂" in msg or "蒂蒂抱" in msg:
            responses = ["离我那么近......我，我可没有能完全保护你的自信！",
                         "博士......来这里。",
                         "好，好吧，不要让别人看见哦~"]
            return choice(responses)

        if "亲蒂蒂" in msg or "蒂蒂亲" in msg:
            responses = ["听你的。",
                         "离我那么近......我，我可没有能完全保护你的自信！",
                         "好，好吧，不要让别人看见哦~"]
            return choice(responses)
        
        if "爱蒂蒂" in msg or "蒂蒂爱" in msg:
            responses = ["你这人，怎么这么执着，这样我不就只能老老实实保护你了吗。",
                         "好，又度过了轻松的一天！没有会卷走队友的巨大触须，也没有蹲在角落里满手是血的疯狂敌人......光是上上战场什么的，对，已经很轻松了！",
                         "根据传说，我的族裔已经和那些灾祸战斗了无数年。说不定，我们也帮你们这些城市人把灾祸挡在了陆地之外......所以说，是不是该请我喝一杯，好好谢谢我？"]
            return choice(responses)

        if "蒂蒂早上好" in msg or "蒂蒂早安" in msg:
            responses = ["早安，博士"]
            return choice(responses)

        if "蒂蒂晚上好" in msg or "蒂蒂晚安" in msg:
            responses = ["睡着了？睡吧，博士，得做个干燥的好梦哟。"]
            return choice(responses)

        if "蒂蒂在干什么" in msg or "蒂蒂在干嘛" in msg:
            responses = ["我在等你，博士。我等你太久，太久了，我甚至已经忘了为什么要在这里等你......不过这些都不重要了。不再那么重要了。"]
            return choice(responses)

        if "表白蒂蒂" in msg or "告白蒂蒂" in msg:
            responses = ["真，真的吗？",
                         "我的头发很长，很好看？啊，嗯，谢谢......要不要摸摸看？我的头发还是挺柔软的。这方面，我还算是有些自信的哦。",
                         "斯卡蒂，赏金猎人。你真要签下我？我可是那种，会给你带来灾祸的人哦。"]
            return choice(responses)

        if "为斯卡蒂献出心脏" in msg or "为斯卡蒂献上心脏" in msg:
            responses = ["撒撒给呦~撒撒给呦~心脏~撒撒给呦~"]
            return choice(responses)

        if "蒂蒂贴" in msg or "贴蒂蒂" in msg:
            responses = ["啊......帽子！",
                         "离我那么近......我，我可没有能完全保护你的自信！",
                         "和博士贴贴~！"]
            return choice(responses)
        
        if "草" in msg:
            responses = ["一种植物。"]
            return choice(responses)

        if "艹" in msg:
            responses = ["一种地形。"]
            return choice(responses)
        
        # 发送多条信息并且在过程中休眠
        if "撒撒给呦" in msg:
            await chat.send("撒撒给呦~")
            await asyncio.sleep(1)
            await chat.send("心脏~")
            await asyncio.sleep(1)
            await chat.send("撒撒给呦~")
            await asyncio.sleep(1)
            return r'为斯卡蒂！献上心脏！'

    # 添加响应概率不同的事件
    if (cool_down(group_id) and random_response(p=20)) or is_super_user:
        if "？" == msg or "?" == msg:
            responses = ['？',
                         '¿',
                         '？？',
                         '？？？',
                         '当我打出问号的时候，不是我有问题，而是我觉得你有问题']             
            return choice(responses)
