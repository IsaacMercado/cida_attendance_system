from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRANSFER_SWITCH(Structure):
    pass

_S(struct_tagNET_DVR_TRANSFER_SWITCH, [
    ('dwEnable', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_TRANSFER_SWITCH = struct_tagNET_DVR_TRANSFER_SWITCH
LPNET_DVR_TRANSFER_SWITCH = POINTER(struct_tagNET_DVR_TRANSFER_SWITCH)
tagNET_DVR_TRANSFER_SWITCH = struct_tagNET_DVR_TRANSFER_SWITCH
