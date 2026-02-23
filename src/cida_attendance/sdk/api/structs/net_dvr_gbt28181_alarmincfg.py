from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GBT28181_ALARMINCFG(Structure):
    pass

_S(struct_tagNET_DVR_GBT28181_ALARMINCFG, [
    ('dwSize', DWORD),
    ('szAlarmInNumID', c_char * 64),
    ('byRes', BYTE * 256),
])

NET_DVR_GBT28181_ALARMINCFG = struct_tagNET_DVR_GBT28181_ALARMINCFG
LPNET_DVR_GBT28181_ALARMINCFG = POINTER(struct_tagNET_DVR_GBT28181_ALARMINCFG)
tagNET_DVR_GBT28181_ALARMINCFG = struct_tagNET_DVR_GBT28181_ALARMINCFG
