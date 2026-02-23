from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NAS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_NAS_PARAM, [
    ('dwSize', DWORD),
    ('dwLunID', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_NAS_PARAM = struct_tagNET_DVR_NAS_PARAM
LPNET_DVR_NAS_PARAM = POINTER(struct_tagNET_DVR_NAS_PARAM)
tagNET_DVR_NAS_PARAM = struct_tagNET_DVR_NAS_PARAM
