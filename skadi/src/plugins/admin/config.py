
# from typing import Optional
from nonebot import get_driver
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    callback_notice: bool = False # 是否在操作完成后在 QQ 返回提示


global_config = get_driver().config
plugin_config = Config.parse_obj(global_config)
