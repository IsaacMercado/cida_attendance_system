from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMMODECFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMMODECFG, [
    ('dwSize', DWORD),
    ('byAlarmMode', BYTE),
    ('wLoopTime', WORD),
    ('byRes', BYTE * 9),
])

NET_DVR_ALARMMODECFG = struct_tagNET_DVR_ALARMMODECFG
LPNET_DVR_ALARMMODECFG = POINTER(struct_tagNET_DVR_ALARMMODECFG)
tagNET_DVR_ALARMMODECFG = struct_tagNET_DVR_ALARMMODECFG
