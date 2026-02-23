from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OBJECT_FEATURE(Structure):
    pass

_S(struct_tagNET_DVR_OBJECT_FEATURE, [
    ('byColorRatel', BYTE),
    ('byRed', BYTE),
    ('byGreen', BYTE),
    ('byBlue', BYTE),
    ('byRes', BYTE * 32),
])

NET_DVR_OBJECT_FEATURE = struct_tagNET_DVR_OBJECT_FEATURE
LPNET_DVR_OBJECT_FEATURE = POINTER(struct_tagNET_DVR_OBJECT_FEATURE)
tagNET_DVR_OBJECT_FEATURE = struct_tagNET_DVR_OBJECT_FEATURE
