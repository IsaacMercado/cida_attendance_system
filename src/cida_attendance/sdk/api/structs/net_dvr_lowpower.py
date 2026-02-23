from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_386 import NET_DVR_SCHEDULE_DAYTIME


class struct_tagNET_DVR_LOWPOWER(Structure):
    pass

_S(struct_tagNET_DVR_LOWPOWER, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byEnabled', BYTE),
    ('byRes', BYTE * 6),
    ('struSchedTime', NET_DVR_SCHEDULE_DAYTIME),
    ('byRes1', BYTE * 256),
])

NET_DVR_LOWPOWER = struct_tagNET_DVR_LOWPOWER
LPNET_DVR_LOWPOWER = POINTER(struct_tagNET_DVR_LOWPOWER)
tagNET_DVR_LOWPOWER = struct_tagNET_DVR_LOWPOWER
