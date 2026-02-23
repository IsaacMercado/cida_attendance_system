from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TERMINAL_INPUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_INPUT_CFG, [
    ('dwSize', DWORD),
    ('dwInputNo', DWORD),
    ('byStreamType', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_TERMINAL_INPUT_CFG = struct_tagNET_DVR_TERMINAL_INPUT_CFG
LPNET_DVR_TERMINAL_INPUT_CFG = POINTER(struct_tagNET_DVR_TERMINAL_INPUT_CFG)
tagNET_DVR_TERMINAL_INPUT_CFG = struct_tagNET_DVR_TERMINAL_INPUT_CFG
