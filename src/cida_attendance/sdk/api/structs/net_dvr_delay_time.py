from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DELAY_TIME(Structure):
    pass

_S(struct_tagNET_DVR_DELAY_TIME, [
    ('dwSize', DWORD),
    ('dwDelayTime', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_DELAY_TIME = struct_tagNET_DVR_DELAY_TIME
LPNET_DVR_DELAY_TIME = POINTER(struct_tagNET_DVR_DELAY_TIME)
tagNET_DVR_DELAY_TIME = struct_tagNET_DVR_DELAY_TIME
