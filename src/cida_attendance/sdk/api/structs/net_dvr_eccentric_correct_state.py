from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ECCENTRIC_CORRECT_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ECCENTRIC_CORRECT_STATE, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byEccentricCorrectState', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_ECCENTRIC_CORRECT_STATE = struct_tagNET_DVR_ECCENTRIC_CORRECT_STATE
LPNET_DVR_ECCENTRIC_CORRECT_STATE = POINTER(struct_tagNET_DVR_ECCENTRIC_CORRECT_STATE)
tagNET_DVR_ECCENTRIC_CORRECT_STATE = struct_tagNET_DVR_ECCENTRIC_CORRECT_STATE
