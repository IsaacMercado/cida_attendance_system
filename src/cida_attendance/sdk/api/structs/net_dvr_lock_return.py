from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_LOCK_RETURN(Structure):
    pass

_S(struct_tagNET_DVR_LOCK_RETURN, [
    ('dwSize', DWORD),
    ('strBeginTime', NET_DVR_TIME),
    ('strEndTime', NET_DVR_TIME),
    ('byISO8601', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 17),
])

NET_DVR_LOCK_RETURN = struct_tagNET_DVR_LOCK_RETURN
LPNET_DVR_LOCK_RETURN = POINTER(struct_tagNET_DVR_LOCK_RETURN)
tagNET_DVR_LOCK_RETURN = struct_tagNET_DVR_LOCK_RETURN
