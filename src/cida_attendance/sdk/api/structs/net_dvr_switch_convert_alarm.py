from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SWITCH_CONVERT_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_SWITCH_CONVERT_ALARM, [
    ('dwSize', DWORD),
    ('byPortNo', BYTE),
    ('byPortNoEx', BYTE),
    ('byRes1', BYTE * 2),
    ('dwEventType', DWORD),
    ('dwEvent', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_SWITCH_CONVERT_ALARM = struct_tagNET_DVR_SWITCH_CONVERT_ALARM
LPNET_DVR_SWITCH_CONVERT_ALARM = POINTER(struct_tagNET_DVR_SWITCH_CONVERT_ALARM)
tagNET_DVR_SWITCH_CONVERT_ALARM = struct_tagNET_DVR_SWITCH_CONVERT_ALARM
