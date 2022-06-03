from ast import alias
from random import choice
import re
from urllib import response
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, Message

#蒂蒂的聊天插件，采用comman触发，防止误触，random生成随机数来返回随机信息
bao = on_command('抱')
@bao.handle()
async def handle_bao():
    responses = ["离我那么近......我，我可没有能完全保护你的自信！",
                 "博士......来这里。",
                 "好，好吧，不要让别人看见哦~"]
    msg = choice(responses)
    await bao.finish(msg)

kiss = on_command('亲亲')
@kiss.handle()
async def handle_kiss():
    responses = ["听你的。",
                 "离我那么近......我，我可没有能完全保护你的自信！",
                 "好，好吧，不要让别人看见哦~"]
    msg = choice(responses)
    await kiss.finish(msg)

love = on_command('爱')
@love.handle()
async def handle_love():
    responses = ["你这人，怎么这么执着，这样我不就只能老老实实保护你了吗。",
                 "好，又度过了轻松的一天！没有会卷走队友的巨大触须，也没有蹲在角落里满手是血的疯狂敌人......光是上上战场什么的，对，已经很轻松了！",
                 "根据传说，我的族裔已经和那些灾祸战斗了无数年。说不定，我们也帮你们这些城市人把灾祸挡在了陆地之外......所以说，是不是该请我喝一杯，好好谢谢我？"]
    msg = choice(responses)
    await love.finish(msg)

morning = on_command('早')
@morning.handle()
async def handle_mornig():
    responses = ["早安，博士"]
    msg = choice(responses)
    await morning.finish(msg)

night = on_command('晚')
@night.handle()
async def handle_night():
    responses = ["睡着了？睡吧，博士，得做个干燥的好梦哟。"]
    msg = choice(responses)
    await night.finish(msg)

what = on_command("干什么",aliases={"干嘛"})
@what.handle()
async def handle_what():
    responses = ["我在等你，博士。我等你太久，太久了，我甚至已经忘了为什么要在这里等你......不过这些都不重要了。不再那么重要了。"]
    msg = choice(responses)
    await what.finish(msg)

express = on_command("告白",aliases={"表白"})
@express.handle()
async def handle_express():
    responses = ["真，真的吗？",
                 "我的头发很长，很好看？啊，嗯，谢谢......要不要摸摸看？我的头发还是挺柔软的。这方面，我还算是有些自信的哦。",
                 "斯卡蒂，赏金猎人。你真要签下我？我可是那种，会给你带来灾祸的人哦。"]
    msg = choice(responses)
    await express.finish(msg)

tietie = on_command('贴贴')
@tietie.handle()
async def handle_tietie():
    responses = ["啊......帽子！",
                         "离我那么近......我，我可没有能完全保护你的自信！",
                         "和博士贴贴~！"]
    msg = choice(responses)
    await tietie.finish(msg)

xinzang = on_command("献上心脏", aliases={"献出心脏"})
@xinzang.handle()
async def handle_xinzang():
    response = ["撒撒给呦~撒撒给呦~心脏~撒撒给呦~"]
    msg = choice(response)
    await xinzang.finish(msg)