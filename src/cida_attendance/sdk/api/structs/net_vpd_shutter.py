from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VPD_SHUTTER(Structure):
    pass

_S(struct_tagNET_VPD_SHUTTER, [
    ('dwCommmand', DWORD),
    ('dwCode', DWORD),
    ('byRes', BYTE * 60),
])

NET_VPD_SHUTTER = struct_tagNET_VPD_SHUTTER
LPNET_VPD_SHUTTER = POINTER(struct_tagNET_VPD_SHUTTER)
tagNET_VPD_SHUTTER = struct_tagNET_VPD_SHUTTER
