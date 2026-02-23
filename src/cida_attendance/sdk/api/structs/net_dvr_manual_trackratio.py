from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MANUAL_TRACKRATIO(Structure):
    pass

_S(struct_tagNET_DVR_MANUAL_TRACKRATIO, [
    ('dwSize', DWORD),
    ('byCoefficient', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_MANUAL_TRACKRATIO = struct_tagNET_DVR_MANUAL_TRACKRATIO
LPNET_DVR_MANUAL_TRACKRATIO = POINTER(struct_tagNET_DVR_MANUAL_TRACKRATIO)
tagNET_DVR_MANUAL_TRACKRATIO = struct_tagNET_DVR_MANUAL_TRACKRATIO
