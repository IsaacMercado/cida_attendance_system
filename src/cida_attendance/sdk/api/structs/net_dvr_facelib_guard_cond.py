from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACELIB_GUARD_COND(Structure):
    pass

_S(struct_tagNET_DVR_FACELIB_GUARD_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('szFDID', c_char * 68),
    ('byRes', BYTE * 128),
])

NET_DVR_FACELIB_GUARD_COND = struct_tagNET_DVR_FACELIB_GUARD_COND
LPNET_DVR_FACELIB_GUARD_COND = POINTER(struct_tagNET_DVR_FACELIB_GUARD_COND)
tagNET_DVR_FACELIB_GUARD_COND = struct_tagNET_DVR_FACELIB_GUARD_COND
