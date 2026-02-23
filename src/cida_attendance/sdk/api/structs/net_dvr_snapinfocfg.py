from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SNAPINFOCFG(Structure):
    pass

_S(struct_tagNET_DVR_SNAPINFOCFG, [
    ('dwSize', DWORD),
    ('byCurPicType', BYTE),
    ('byPicQuality', BYTE),
    ('byRes1', BYTE * 2),
    ('dwPicSize', DWORD),
    ('byRes2', BYTE * 128),
])

NET_DVR_SNAPINFOCFG = struct_tagNET_DVR_SNAPINFOCFG
LPNET_DVR_SNAPINFOCFG = POINTER(struct_tagNET_DVR_SNAPINFOCFG)
tagNET_DVR_SNAPINFOCFG = struct_tagNET_DVR_SNAPINFOCFG
