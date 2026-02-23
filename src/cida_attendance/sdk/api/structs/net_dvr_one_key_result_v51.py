from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONE_KEY_RESULT_V51(Structure):
    pass

_S(struct_tagNET_DVR_ONE_KEY_RESULT_V51, [
    ('dwState', DWORD),
    ('byProgress', BYTE),
    ('byRes', BYTE * 259),
])

NET_DVR_ONE_KEY_RESULT_V51 = struct_tagNET_DVR_ONE_KEY_RESULT_V51
LPNET_DVR_ONE_KEY_RESULT_V51 = POINTER(struct_tagNET_DVR_ONE_KEY_RESULT_V51)
tagNET_DVR_ONE_KEY_RESULT_V51 = struct_tagNET_DVR_ONE_KEY_RESULT_V51
