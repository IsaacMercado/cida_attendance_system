from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LAMP_STATE(Structure):
    pass

_S(struct_tagNET_DVR_LAMP_STATE, [
    ('byFlicker', BYTE),
    ('byParkingIndex', BYTE),
    ('byRes1', BYTE * 2),
    ('dwIONo', DWORD),
    ('byRes2', BYTE * 8),
])

NET_DVR_LAMP_STATE = struct_tagNET_DVR_LAMP_STATE
LPNET_DVR_LAMP_STATE = POINTER(struct_tagNET_DVR_LAMP_STATE)
tagNET_DVR_LAMP_STATE = struct_tagNET_DVR_LAMP_STATE
