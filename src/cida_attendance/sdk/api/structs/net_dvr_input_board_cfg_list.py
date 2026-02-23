from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_input_board_cfg import NET_DVR_INPUT_BOARD_CFG


class struct_tagNET_DVR_INPUT_BOARD_CFG_LIST(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_BOARD_CFG_LIST, [
    ('dwSize', DWORD),
    ('struBoardList', NET_DVR_INPUT_BOARD_CFG * 512),
])

NET_DVR_INPUT_BOARD_CFG_LIST = struct_tagNET_DVR_INPUT_BOARD_CFG_LIST
LPNET_DVR_INPUT_BOARD_CFG_LIST = POINTER(struct_tagNET_DVR_INPUT_BOARD_CFG_LIST)
tagNET_DVR_INPUT_BOARD_CFG_LIST = struct_tagNET_DVR_INPUT_BOARD_CFG_LIST
