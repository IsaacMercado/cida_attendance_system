from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FIRMWARECODE_COND(Structure):
    pass

_S(struct_tagNET_DVR_FIRMWARECODE_COND, [
    ('dwSize', DWORD),
    ('dwStartIndex', DWORD),
    ('dwMaxNum', DWORD),
    ('byRes', BYTE * 52),
])

NET_DVR_FIRMWARECODE_COND = struct_tagNET_DVR_FIRMWARECODE_COND
LPNET_DVR_FIRMWARECODE_COND = POINTER(struct_tagNET_DVR_FIRMWARECODE_COND)
tagNET_DVR_FIRMWARECODE_COND = struct_tagNET_DVR_FIRMWARECODE_COND
