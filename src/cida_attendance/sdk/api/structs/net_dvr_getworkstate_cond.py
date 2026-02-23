from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GETWORKSTATE_COND(Structure):
    pass

_S(struct_tagNET_DVR_GETWORKSTATE_COND, [
    ('dwSize', DWORD),
    ('byFindHardByCond', BYTE),
    ('byFindChanByCond', BYTE),
    ('byRes1', BYTE * 2),
    ('dwFindHardStatus', DWORD * 33),
    ('dwFindChanNo', DWORD * 512),
    ('byRes', BYTE * 64),
])

NET_DVR_GETWORKSTATE_COND = struct_tagNET_DVR_GETWORKSTATE_COND
LPNET_DVR_GETWORKSTATE_COND = POINTER(struct_tagNET_DVR_GETWORKSTATE_COND)
tagNET_DVR_GETWORKSTATE_COND = struct_tagNET_DVR_GETWORKSTATE_COND
