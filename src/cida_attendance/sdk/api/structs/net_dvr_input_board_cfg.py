from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUT_BOARD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_BOARD_CFG, [
    ('dwSize', DWORD),
    ('dwSlotNo', DWORD),
    ('byFullFrameEnable', BYTE),
    ('byRes', BYTE * 3),
    ('byRes1', BYTE * 64),
])

NET_DVR_INPUT_BOARD_CFG = struct_tagNET_DVR_INPUT_BOARD_CFG
LPNET_DVR_INPUT_BOARD_CFG = POINTER(struct_tagNET_DVR_INPUT_BOARD_CFG)
tagNET_DVR_INPUT_BOARD_CFG = struct_tagNET_DVR_INPUT_BOARD_CFG
