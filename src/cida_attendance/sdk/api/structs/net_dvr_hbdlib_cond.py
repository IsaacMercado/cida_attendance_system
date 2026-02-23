from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HBDLIB_COND(Structure):
    pass

_S(struct_tagNET_DVR_HBDLIB_COND, [
    ('dwSize', DWORD),
    ('szHBDID', c_char * 256),
    ('byConcurrent', BYTE),
    ('byCover', BYTE),
    ('byCustomHBDID', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_HBDLIB_COND = struct_tagNET_DVR_HBDLIB_COND
LPNET_DVR_HBDLIB_COND = POINTER(struct_tagNET_DVR_HBDLIB_COND)
tagNET_DVR_HBDLIB_COND = struct_tagNET_DVR_HBDLIB_COND
