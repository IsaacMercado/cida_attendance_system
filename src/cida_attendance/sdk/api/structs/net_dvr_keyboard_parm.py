from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_KEYBOARD_PARM(Structure):
    pass

_S(struct_tagNET_DVR_KEYBOARD_PARM, [
    ('dwKeyValue', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_KEYBOARD_PARAM = struct_tagNET_DVR_KEYBOARD_PARM
LPNET_DVR_KEYBOARD_PARAM = POINTER(struct_tagNET_DVR_KEYBOARD_PARM)
tagNET_DVR_KEYBOARD_PARM = struct_tagNET_DVR_KEYBOARD_PARM
