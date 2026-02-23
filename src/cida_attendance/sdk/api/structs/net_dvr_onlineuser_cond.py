from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONLINEUSER_COND(Structure):
    pass

_S(struct_tagNET_DVR_ONLINEUSER_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_ONLINEUSER_COND = struct_tagNET_DVR_ONLINEUSER_COND
LPNET_DVR_ONLINEUSER_COND = POINTER(struct_tagNET_DVR_ONLINEUSER_COND)
tagNET_DVR_ONLINEUSER_COND = struct_tagNET_DVR_ONLINEUSER_COND
