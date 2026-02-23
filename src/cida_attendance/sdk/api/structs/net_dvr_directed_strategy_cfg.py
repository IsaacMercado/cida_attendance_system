from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DIRECTED_STRATEGY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DIRECTED_STRATEGY_CFG, [
    ('dwSize', DWORD),
    ('byDirectedStrategyType', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_DIRECTED_STRATEGY_CFG = struct_tagNET_DVR_DIRECTED_STRATEGY_CFG
LPNET_DVR_DIRECTED_STRATEGY_CFG = POINTER(struct_tagNET_DVR_DIRECTED_STRATEGY_CFG)
tagNET_DVR_DIRECTED_STRATEGY_CFG = struct_tagNET_DVR_DIRECTED_STRATEGY_CFG
