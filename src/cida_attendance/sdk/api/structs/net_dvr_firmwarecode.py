from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FIRMWARECODE(Structure):
    pass

_S(struct_tagNET_DVR_FIRMWARECODE, [
    ('wIndex', WORD),
    ('wCodeLen', WORD),
    ('byCode', BYTE * 128),
    ('byVersion', BYTE * 64),
    ('byRes', BYTE * 12),
])

NET_DVR_FIRMWARECODE = struct_tagNET_DVR_FIRMWARECODE
LPNET_DVR_FIRMWARECODE = POINTER(struct_tagNET_DVR_FIRMWARECODE)
tagNET_DVR_FIRMWARECODE = struct_tagNET_DVR_FIRMWARECODE
