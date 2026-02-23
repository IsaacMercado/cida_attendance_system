from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SHOW_CONTROL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SHOW_CONTROL_INFO, [
    ('dwSize', DWORD),
    ('dwDisplayNo', DWORD),
    ('byEnable', BYTE),
    ('byChanType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwWallNo', DWORD),
    ('byRes2', BYTE * 56),
])

NET_DVR_SHOW_CONTROL_INFO = struct_tagNET_DVR_SHOW_CONTROL_INFO
LPNET_DVR_SHOW_CONTROL_INFO = POINTER(struct_tagNET_DVR_SHOW_CONTROL_INFO)
tagNET_DVR_SHOW_CONTROL_INFO = struct_tagNET_DVR_SHOW_CONTROL_INFO
