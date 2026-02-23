from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREENALARMCFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREENALARMCFG, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byBoardType', BYTE),
    ('bySubException', BYTE),
    ('byRes1', BYTE),
    ('wStartInputNum', WORD),
    ('wEndInputNum', WORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_SCREENALARMCFG = struct_tagNET_DVR_SCREENALARMCFG
LPNET_DVR_SCREENALARMCFG = POINTER(struct_tagNET_DVR_SCREENALARMCFG)
tagNET_DVR_SCREENALARMCFG = struct_tagNET_DVR_SCREENALARMCFG
