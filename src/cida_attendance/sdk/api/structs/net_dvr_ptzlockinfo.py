from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZLOCKINFO(Structure):
    pass

_S(struct_tagNET_DVR_PTZLOCKINFO, [
    ('dwSize', DWORD),
    ('dwRemainingSec', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_PTZLOCKINFO = struct_tagNET_DVR_PTZLOCKINFO
LPNET_DVR_PTZLOCKINFO = POINTER(struct_tagNET_DVR_PTZLOCKINFO)
tagNET_DVR_PTZLOCKINFO = struct_tagNET_DVR_PTZLOCKINFO
