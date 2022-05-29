import os
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from nonebot.adapters.onebot.v11 import MessageSegment

#语音包指令

#语音包1
cmd1 = on_command('语音1',aliases={'语音包1'},priority=2,block=True)
@cmd1.handle()
async def cmd1_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi01.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd2 = on_command('语音2',aliases={'语音包2'},priority=2,block=True)
@cmd2.handle()
async def cmd2_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi02.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd3 = on_command('语音3',aliases={'语音包3'},priority=2,block=True)
@cmd3.handle()
async def cmd3_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi03.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd4 = on_command('语音4',aliases={'语音包4'},priority=2,block=True)
@cmd4.handle()
async def cmd4_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi04.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd5 = on_command('语音5',aliases={'语音包5'},priority=2,block=True)
@cmd5.handle()
async def cmd5_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi05.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd6 = on_command('语音6',aliases={'语音包6'},priority=2,block=True)
@cmd6.handle()
async def cmd6_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi06.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd7 = on_command('语音7',aliases={'语音包7'},priority=2,block=True)
@cmd7.handle()
async def cmd7_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi07.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd8 = on_command('语音8',aliases={'语音包8'},priority=2,block=True)
@cmd8.handle()
async def cmd8_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi08.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd9 = on_command('语音9',aliases={'语音包9'},priority=2,block=True)
@cmd9.handle()
async def cmd9_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi09.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd10 = on_command('语音10',aliases={'语音包10'},priority=2,block=True)
@cmd10.handle()
async def cmd10_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi10.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd11 = on_command('语音11',aliases={'语音包11'},priority=2,block=True)
@cmd11.handle()
async def cmd11_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi11.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd12 = on_command('语音12',aliases={'语音包12'},priority=2,block=True)
@cmd12.handle()
async def cmd12_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi12.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd13 = on_command('语音13',aliases={'语音包13'},priority=2,block=True)
@cmd13.handle()
async def cmd13_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi13.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd14 = on_command('语音14',aliases={'语音包14'},priority=2,block=True)
@cmd14.handle()
async def cmd14_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi14.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd15 = on_command('语音15',aliases={'语音包15'},priority=2,block=True)
@cmd15.handle()
async def cmd15_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi15.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd16 = on_command('语音16',aliases={'语音包16'},priority=2,block=True)
@cmd16.handle()
async def cmd16_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi16.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd17 = on_command('语音17',aliases={'语音包17'},priority=2,block=True)
@cmd17.handle()
async def cmd12_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi17.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd18 = on_command('语音18',aliases={'语音包18'},priority=2,block=True)
@cmd18.handle()
async def cmd18_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi18.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd19 = on_command('语音19',aliases={'语音包19'},priority=2,block=True)
@cmd19.handle()
async def cmd19_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi19.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd20 = on_command('语音20',aliases={'语音包20'},priority=2,block=True)
@cmd20.handle()
async def cmd20_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi20.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd21 = on_command('语音21',aliases={'语音包21'},priority=2,block=True)
@cmd21.handle()
async def cmd21_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi21.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd22 = on_command('语音22',aliases={'语音包22'},priority=2,block=True)
@cmd22.handle()
async def cmd22_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi22.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd23 = on_command('语音23',aliases={'语音包23'},priority=2,block=True)
@cmd23.handle()
async def cmd23_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi23.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd24 = on_command('语音24',aliases={'语音包24'},priority=2,block=True)
@cmd24.handle()
async def cmd24_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi24.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd25 = on_command('语音25',aliases={'语音包25'},priority=2,block=True)
@cmd25.handle()
async def cmd25_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi25.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd26 = on_command('语音26',aliases={'语音包26'},priority=2,block=True)
@cmd26.handle()
async def cmd26_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi26.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd27 = on_command('语音27',aliases={'语音包27'},priority=2,block=True)
@cmd27.handle()
async def cmd20_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi27.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd28 = on_command('语音28',aliases={'语音包28'},priority=2,block=True)
@cmd28.handle()
async def cmd28_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi28.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd29 = on_command('语音29',aliases={'语音包29'},priority=2,block=True)
@cmd29.handle()
async def cmd29_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi29.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd30 = on_command('语音30',aliases={'语音包30'},priority=2,block=True)
@cmd30.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi30.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd31 = on_command('语音31',aliases={'语音包31'},priority=2,block=True)
@cmd31.handle()
async def cmd31_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi31.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd32 = on_command('语音32',aliases={'语音包32'},priority=2,block=True)
@cmd32.handle()
async def cmd32_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi32.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd33 = on_command('语音33',aliases={'语音包33'},priority=2,block=True)
@cmd33.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi33.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd34 = on_command('语音34',aliases={'语音包34'},priority=2,block=True)
@cmd34.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi34.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd35 = on_command('语音35',aliases={'语音包35'},priority=2,block=True)
@cmd35.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi35.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd36 = on_command('语音36',aliases={'语音包36'},priority=2,block=True)
@cmd36.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi36.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd37 = on_command('语音37',aliases={'语音包37'},priority=2,block=True)
@cmd37.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi37.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd38 = on_command('语音38',aliases={'语音包38'},priority=2,block=True)
@cmd38.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi38.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd39 = on_command('语音39',aliases={'语音包39'},priority=2,block=True)
@cmd39.handle()
async def cmd39_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi39.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd40 = on_command('语音40',aliases={'语音包40'},priority=2,block=True)
@cmd40.handle()
async def cmd40_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi40.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd41 = on_command('语音41',aliases={'语音包41'},priority=2,block=True)
@cmd41.handle()
async def cmd41_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi41.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd42 = on_command('语音42',aliases={'语音包42'},priority=2,block=True)
@cmd42.handle()
async def cmd40_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi42.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd43 = on_command('语音43',aliases={'语音包43'},priority=2,block=True)
@cmd43.handle()
async def cmd43_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi43.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd44 = on_command('语音44',aliases={'语音包44'},priority=2,block=True)
@cmd44.handle()
async def cmd44_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi44.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd45 = on_command('语音45',aliases={'语音包45'},priority=2,block=True)
@cmd45.handle()
async def cmd45_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi45.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd46 = on_command('语音46',aliases={'语音包46'},priority=2,block=True)
@cmd46.handle()
async def cmd46_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi46.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd47 = on_command('语音47',aliases={'语音包47'},priority=2,block=True)
@cmd47.handle()
async def cmd47_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi47.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd48 = on_command('语音48',aliases={'语音包48'},priority=2,block=True)
@cmd48.handle()
async def cmd48_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi48.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd49 = on_command('语音49',aliases={'语音包49'},priority=2,block=True)
@cmd49.handle()
async def cmd49_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi49.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd50 = on_command('语音50',aliases={'语音包50'},priority=2,block=True)
@cmd50.handle()
async def cmd50_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi50.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd51 = on_command('语音51',aliases={'语音包51'},priority=2,block=True)
@cmd51.handle()
async def cmd51_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi51.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd52 = on_command('语音52',aliases={'语音包52'},priority=2,block=True)
@cmd52.handle()
async def cmd52_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi52.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd53 = on_command('语音53',aliases={'语音包53'},priority=2,block=True)
@cmd53.handle()
async def cmd53_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi53.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd54 = on_command('语音54',aliases={'语音包54'},priority=2,block=True)
@cmd54.handle()
async def cmd54_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi54.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd55 = on_command('语音55',aliases={'语音包55'},priority=2,block=True)
@cmd55.handle()
async def cmd55_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi55.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd56 = on_command('语音56',aliases={'语音包56'},priority=2,block=True)
@cmd56.handle()
async def cmd56_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi56.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd57 = on_command('语音57',aliases={'语音包57'},priority=2,block=True)
@cmd57.handle()
async def cmd57_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi5.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd58 = on_command('语音58',aliases={'语音包58'},priority=2,block=True)
@cmd58.handle()
async def cmd58_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi58.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd59 = on_command('语音59',aliases={'语音包59'},priority=2,block=True)
@cmd59.handle()
async def cmd59_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi59.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd60 = on_command('语音60',aliases={'语音包60'},priority=2,block=True)
@cmd60.handle()
async def cmd60_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi60.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd61 = on_command('语音61',aliases={'语音包61'},priority=2,block=True)
@cmd61.handle()
async def cmd61_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi61.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd62 = on_command('语音62',aliases={'语音包62'},priority=2,block=True)
@cmd62.handle()
async def cmd60_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi62.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )
        
cmd63 = on_command('语音63',aliases={'语音包63'},priority=2,block=True)
@cmd63.handle()
async def cmd63_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi63.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd64 = on_command('语音64',aliases={'语音包64'},priority=2,block=True)
@cmd64.handle()
async def cmd64_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi64.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd65 = on_command('语音65',aliases={'语音包65'},priority=2,block=True)
@cmd65.handle()
async def cmd65_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi65.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd66 = on_command('语音66',aliases={'语音包66'},priority=2,block=True)
@cmd66.handle()
async def cmd66_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi66.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd67 = on_command('语音67',aliases={'语音包67'},priority=2,block=True)
@cmd67.handle()
async def cmd67_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi67.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd68 = on_command('语音68',aliases={'语音包68'},priority=2,block=True)
@cmd68.handle()
async def cmd68_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi68.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd69 = on_command('语音69',aliases={'语音包69'},priority=2,block=True)
@cmd69.handle()
async def cmd69_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi69.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd70 = on_command('语音70',aliases={'语音包70'},priority=2,block=True)
@cmd70.handle()
async def cmd70_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\skadi70.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd71 = on_command('语音42姐',aliases={'语音包42姐','语音史尔特尔1','语音包史尔特尔1'},priority=2,block=True)
@cmd71.handle()
async def cmd71_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\surtr1.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd72 = on_command('语音莱瓦汀',aliases={'语音包莱万汀','语音史尔特尔2','语音包史尔特尔2','语音莱万汀','语音包莱瓦汀'},priority=2,block=True)
@cmd72.handle()
async def cmd72_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\surtr2.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )