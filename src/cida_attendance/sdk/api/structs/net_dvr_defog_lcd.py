from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEFOG_LCD(Structure):
    pass

_S(struct_tagNET_DVR_DEFOG_LCD, [
    ('dwSize', DWORD),
    ('byDefogEnable', BYTE),
    ('byDefogModel', BYTE),
    ('byDefogLevel', BYTE),
    ('byRes', BYTE * 33),
])

NET_DVR_DEFOG_LCD = struct_tagNET_DVR_DEFOG_LCD
LPNET_DVR_DEFOG_LCD = POINTER(struct_tagNET_DVR_DEFOG_LCD)
tagNET_DVR_DEFOG_LCD = struct_tagNET_DVR_DEFOG_LCD
