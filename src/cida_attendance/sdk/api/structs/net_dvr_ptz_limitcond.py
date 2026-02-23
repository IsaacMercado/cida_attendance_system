from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_LIMITCOND(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_LIMITCOND, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byLimitMode', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_PTZ_LIMITCOND = struct_tagNET_DVR_PTZ_LIMITCOND
LPNET_DVR_PTZ_LIMITCOND = POINTER(struct_tagNET_DVR_PTZ_LIMITCOND)
tagNET_DVR_PTZ_LIMITCOND = struct_tagNET_DVR_PTZ_LIMITCOND
