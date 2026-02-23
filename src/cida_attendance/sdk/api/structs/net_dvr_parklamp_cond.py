from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARKLAMP_COND(Structure):
    pass

_S(struct_tagNET_DVR_PARKLAMP_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byParkingIndex', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_PARKLAMP_COND = struct_tagNET_DVR_PARKLAMP_COND
LPNET_DVR_PARKLAMP_COND = POINTER(struct_tagNET_DVR_PARKLAMP_COND)
tagNET_DVR_PARKLAMP_COND = struct_tagNET_DVR_PARKLAMP_COND
