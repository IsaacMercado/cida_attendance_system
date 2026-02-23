from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PINSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_PINSTATUS, [
    ('dwSize', DWORD),
    ('byStatus', BYTE),
    ('byPinTimes', BYTE),
    ('byPukTimes', BYTE),
    ('bEnableLock', BYTE),
    ('byRes', BYTE * 4),
])

NET_DVR_PINSTATUS = struct_tagNET_DVR_PINSTATUS
LPNET_DVR_PINSTATUS = POINTER(struct_tagNET_DVR_PINSTATUS)
tagNET_DVR_PINSTATUS = struct_tagNET_DVR_PINSTATUS
