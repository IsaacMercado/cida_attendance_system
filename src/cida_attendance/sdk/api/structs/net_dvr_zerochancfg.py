from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ZEROCHANCFG(Structure):
    pass

_S(struct_tagNET_DVR_ZEROCHANCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwVideoBitrate', DWORD),
    ('dwVideoFrameRate', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_ZEROCHANCFG = struct_tagNET_DVR_ZEROCHANCFG
LPNET_DVR_ZEROCHANCFG = POINTER(struct_tagNET_DVR_ZEROCHANCFG)
tagNET_DVR_ZEROCHANCFG = struct_tagNET_DVR_ZEROCHANCFG
