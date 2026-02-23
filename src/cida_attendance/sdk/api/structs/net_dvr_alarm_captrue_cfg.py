from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_CAPTRUE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_CAPTRUE_CFG, [
    ('dwSize', DWORD),
    ('byBeforeAlarmPic', BYTE),
    ('byAfterAlarmPic', BYTE),
    ('wInterval', WORD),
    ('byResolution', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_ALARM_CAPTRUE_CFG = struct_tagNET_DVR_ALARM_CAPTRUE_CFG
LPNET_DVR_ALARM_CAPTRUE_CFG = POINTER(struct_tagNET_DVR_ALARM_CAPTRUE_CFG)
tagNET_DVR_ALARM_CAPTRUE_CFG = struct_tagNET_DVR_ALARM_CAPTRUE_CFG
