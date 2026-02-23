from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_func_card_state_v50 import NET_DVR_FUNC_CARD_STATE_V50
from .net_dvr_net_card_state_v50 import NET_DVR_NET_CARD_STATE_V50
from .net_dvr_remote_send_card_state_v50 import NET_DVR_REMOTE_SEND_CARD_STATE_V50


class struct_tagNET_DVR_FIBER_CONVERT_STATE_V50(Structure):
    pass

_S(struct_tagNET_DVR_FIBER_CONVERT_STATE_V50, [
    ('dwSize', DWORD),
    ('struNetCardState', NET_DVR_NET_CARD_STATE_V50),
    ('struFuncCardState', NET_DVR_FUNC_CARD_STATE_V50 * 32),
    ('struRemoteSendCardState', NET_DVR_REMOTE_SEND_CARD_STATE_V50 * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_FIBER_CONVERT_STATE_V50 = struct_tagNET_DVR_FIBER_CONVERT_STATE_V50
LPNET_DVR_FIBER_CONVERT_STATE_V50 = POINTER(struct_tagNET_DVR_FIBER_CONVERT_STATE_V50)
tagNET_DVR_FIBER_CONVERT_STATE_V50 = struct_tagNET_DVR_FIBER_CONVERT_STATE_V50
