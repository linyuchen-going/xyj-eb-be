# -*- coding: UTF8 -*-
from .tool import UcpaasTool

tool = UcpaasTool()


def send(mobile: str, code: str):
    return tool.send_sms(mobile, "5103", code)
