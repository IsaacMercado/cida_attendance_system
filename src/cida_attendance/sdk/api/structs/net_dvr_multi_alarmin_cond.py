from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MULTI_ALARMIN_COND(Structure):
    pass

_S(struct_tagNET_DVR_MULTI_ALARMIN_COND, [
    ('dwSize', DWORD),
    ('iZoneNo', c_int * 64),
    ('byRes', BYTE * 256),
])

NET_DVR_MULTI_ALARMIN_COND = struct_tagNET_DVR_MULTI_ALARMIN_COND
LPNET_DVR_MULTI_ALARMIN_COND = POINTER(struct_tagNET_DVR_MULTI_ALARMIN_COND)
tagNET_DVR_MULTI_ALARMIN_COND = struct_tagNET_DVR_MULTI_ALARMIN_COND
