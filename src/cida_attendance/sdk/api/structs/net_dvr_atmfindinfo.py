from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ATMFINDINFO(Structure):
    pass

_S(struct_tagNET_DVR_ATMFINDINFO, [
    ('byTransactionType', BYTE),
    ('byRes', BYTE * 3),
    ('dwTransationAmount', DWORD),
])

NET_DVR_ATMFINDINFO = struct_tagNET_DVR_ATMFINDINFO
LPNET_DVR_ATMFINDINFO = POINTER(struct_tagNET_DVR_ATMFINDINFO)
tagNET_DVR_ATMFINDINFO = struct_tagNET_DVR_ATMFINDINFO
