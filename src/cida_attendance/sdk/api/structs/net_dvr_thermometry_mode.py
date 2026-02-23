from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMOMETRY_MODE(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_MODE, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byThermometryROIEnabled', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_THERMOMETRY_MODE = struct_tagNET_DVR_THERMOMETRY_MODE
LPNET_DVR_THERMOMETRY_MODE = POINTER(struct_tagNET_DVR_THERMOMETRY_MODE)
tagNET_DVR_THERMOMETRY_MODE = struct_tagNET_DVR_THERMOMETRY_MODE
