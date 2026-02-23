from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_LAMP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_LAMP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE),
    ('wFlashDuration', WORD),
    ('wFlashIntervalTime', WORD),
    ('byRes', BYTE * 510),
])

NET_DVR_ALARM_LAMP_CFG = struct_tagNET_DVR_ALARM_LAMP_CFG
LPNET_DVR_ALARM_LAMP_CFG = POINTER(struct_tagNET_DVR_ALARM_LAMP_CFG)
tagNET_DVR_ALARM_LAMP_CFG = struct_tagNET_DVR_ALARM_LAMP_CFG
