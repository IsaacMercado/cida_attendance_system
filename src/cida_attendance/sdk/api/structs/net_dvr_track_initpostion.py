from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRACK_INITPOSTION(Structure):
    pass

_S(struct_tagNET_DVR_TRACK_INITPOSTION, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byID', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_TRACK_INITPOSTION = struct_tagNET_DVR_TRACK_INITPOSTION
LPNET_DVR_TRACK_INITPOSTION = POINTER(struct_tagNET_DVR_TRACK_INITPOSTION)
tagNET_DVR_TRACK_INITPOSTION = struct_tagNET_DVR_TRACK_INITPOSTION
