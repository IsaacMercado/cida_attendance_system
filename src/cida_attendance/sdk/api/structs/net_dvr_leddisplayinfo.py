from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_348 import union_anon_348


class struct_tagNET_DVR_LEDDISPLAYINFO(Structure):
    pass

_S(struct_tagNET_DVR_LEDDISPLAYINFO, [
    ('dwSize', DWORD),
    ('byAddressType', BYTE),
    ('byRes1', BYTE * 3),
    ('unionServer', union_anon_348),
    ('szDisplayInfo', c_char * 1024),
    ('byRes', BYTE * 128),
])

NET_DVR_LEDDISPLAYINFO = struct_tagNET_DVR_LEDDISPLAYINFO
LPNET_DVR_LEDDISPLAYINFO = POINTER(struct_tagNET_DVR_LEDDISPLAYINFO)
tagNET_DVR_LEDDISPLAYINFO = struct_tagNET_DVR_LEDDISPLAYINFO
