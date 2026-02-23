from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POINT(Structure):
    pass

_S(struct_tagNET_DVR_POINT, [
    ('dwX', DWORD),
    ('dwY', DWORD),
])

NET_DVR_POINT = struct_tagNET_DVR_POINT
LPNET_DVR_POINT = POINTER(struct_tagNET_DVR_POINT)
tagNET_DVR_POINT = struct_tagNET_DVR_POINT
