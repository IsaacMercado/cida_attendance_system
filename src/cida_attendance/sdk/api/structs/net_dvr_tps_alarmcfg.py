from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TPS_ALARMCFG(Structure):
    pass

_S(struct_tagNET_DVR_TPS_ALARMCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwInterval', DWORD),
    ('byRes', BYTE * 248),
])

NET_DVR_TPS_ALARMCFG = struct_tagNET_DVR_TPS_ALARMCFG
LPNET_DVR_TPS_ALARMCFG = POINTER(struct_tagNET_DVR_TPS_ALARMCFG)
tagNET_DVR_TPS_ALARMCFG = struct_tagNET_DVR_TPS_ALARMCFG
