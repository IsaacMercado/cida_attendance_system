from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISPINFO(Structure):
    pass

_S(struct_tagNET_DVR_DISPINFO, [
    ('byChanNums', BYTE),
    ('byStartChan', BYTE),
    ('byRes', BYTE * 2),
    ('dwSupportResolution', DWORD * 32),
])

NET_DVR_DISPINFO = struct_tagNET_DVR_DISPINFO
LPNET_DVR_DISPINFO = POINTER(struct_tagNET_DVR_DISPINFO)
tagNET_DVR_DISPINFO = struct_tagNET_DVR_DISPINFO
