from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_443 import union_anon_443


class struct_tagNET_DVR_CENTER_SERVER_CFG_(Structure):
    pass

_S(struct_tagNET_DVR_CENTER_SERVER_CFG_, [
    ('dwSize', DWORD),
    ('byAddressType', BYTE),
    ('byRes1', BYTE),
    ('wServerPort', WORD),
    ('unionServer', union_anon_443),
    ('wInterval', WORD),
    ('byRes', BYTE * 514),
])

NET_DVR_CENTER_SERVER_CFG = struct_tagNET_DVR_CENTER_SERVER_CFG_
LPNET_DVR_CENTER_SERVER_CFG = POINTER(struct_tagNET_DVR_CENTER_SERVER_CFG_)
tagNET_DVR_CENTER_SERVER_CFG_ = struct_tagNET_DVR_CENTER_SERVER_CFG_
