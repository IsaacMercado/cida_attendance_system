from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMOMETRY_TRIGGER_COND(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_TRIGGER_COND, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('dwPreset', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_THERMOMETRY_TRIGGER_COND = struct_tagNET_DVR_THERMOMETRY_TRIGGER_COND
LPNET_DVR_THERMOMETRY_TRIGGER_COND = POINTER(struct_tagNET_DVR_THERMOMETRY_TRIGGER_COND)
tagNET_DVR_THERMOMETRY_TRIGGER_COND = struct_tagNET_DVR_THERMOMETRY_TRIGGER_COND
