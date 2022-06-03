# skadi_bot

## 基于nonebot的QQ群机器人

****


## 警告！！！
+ 本项目含有:
 * hanyupinyin
 * 命名不规范
 * 代码重复
- 属于常规问题，无需吐槽

## 部署

+ 部署方法:
    * 首先你需要下载go-cq框架，配置框架后进行下一步
    + 打开power shell命令行，输入pip install nb-cli，按下回车，下载nonebot脚手架
    - 打开源码内skadi\.env.prod配置nonebot监听端口使其与go-cq内监听网址端口相同（源码已配置完毕，这里仅作有特殊需求时修改说明）
	- 打开go-cq框架内生成的bat文件，然后切换至源码文件，打开启动.bat
	- 观察日志，若缺少mould请自行百度，大部分解决方法为pip install 你缺少的包名，例如：pip install skadi_bot
+ 大功告成！

## 后续
+ [我的B站主页(后续会出视频教程)](https://space.bilibili.com/494304578)。
+ 有问题请提问issues，请在提问前详阅[提问的智慧](https://github.com/betaseeker/How-To-Ask-Questions)

## 鸣谢
+ 感谢[nonebot2](https://github.com/nonebot/nonebot2)、[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)提供的框架支持
