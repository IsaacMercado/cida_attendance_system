from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_DVR_BUTTON_DOWN_ALARM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BUTTON_DOWN_ALARM_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRes2', BYTE * 24),
])

NET_IPC_BUTTON_DOWN_ALARM_CFG = struct_tagNET_DVR_BUTTON_DOWN_ALARM_CFG
LPNET_IPC_BUTTON_DOWN_ALARM_CFG = POINTER(struct_tagNET_DVR_BUTTON_DOWN_ALARM_CFG)
tagNET_DVR_BUTTON_DOWN_ALARM_CFG = struct_tagNET_DVR_BUTTON_DOWN_ALARM_CFG
