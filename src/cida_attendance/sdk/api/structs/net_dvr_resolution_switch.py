from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RESOLUTION_SWITCH(Structure):
    pass

_S(struct_tagNET_DVR_RESOLUTION_SWITCH, [
    ('dwSize', DWORD),
    ('byResolutionType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_RESOLUTION_SWITCH = struct_tagNET_DVR_RESOLUTION_SWITCH
LPNET_DVR_RESOLUTION_SWITCH = POINTER(struct_tagNET_DVR_RESOLUTION_SWITCH)
tagNET_DVR_RESOLUTION_SWITCH = struct_tagNET_DVR_RESOLUTION_SWITCH
