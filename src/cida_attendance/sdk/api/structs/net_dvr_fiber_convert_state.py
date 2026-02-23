from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_func_card_state import NET_DVR_FUNC_CARD_STATE
from .net_dvr_net_card_state import NET_DVR_NET_CARD_STATE


class struct_tagNET_DVR_FIBER_CONVERT_STATE(Structure):
    pass

_S(struct_tagNET_DVR_FIBER_CONVERT_STATE, [
    ('dwSize', DWORD),
    ('struNetCardState', NET_DVR_NET_CARD_STATE),
    ('struFuncCardState', NET_DVR_FUNC_CARD_STATE * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_FIBER_CONVERT_STATE = struct_tagNET_DVR_FIBER_CONVERT_STATE
LPNET_DVR_FIBER_CONVERT_STATE = POINTER(struct_tagNET_DVR_FIBER_CONVERT_STATE)
tagNET_DVR_FIBER_CONVERT_STATE = struct_tagNET_DVR_FIBER_CONVERT_STATE
