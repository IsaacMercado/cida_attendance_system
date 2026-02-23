from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAPTURE_DATA_COND(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_DATA_COND, [
    ('dwSize', DWORD),
    ('szPassword', c_char * 128),
    ('byRes', BYTE * 128),
])

NET_DVR_CAPTURE_DATA_COND = struct_tagNET_DVR_CAPTURE_DATA_COND
LPNET_DVR_CAPTURE_DATA_COND = POINTER(struct_tagNET_DVR_CAPTURE_DATA_COND)
tagNET_DVR_CAPTURE_DATA_COND = struct_tagNET_DVR_CAPTURE_DATA_COND
