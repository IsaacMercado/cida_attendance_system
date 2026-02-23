from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_func_card_info_v50 import NET_DVR_FUNC_CARD_INFO_V50
from .net_dvr_netmgr_card_info_v50 import NET_DVR_NETMGR_CARD_INFO_V50
from .net_dvr_remote_send_card_info_v50 import NET_DVR_REMOTE_SEND_CARD_INFO_V50


class struct_tagNET_DVR_FIBER_CONVERT_BASIC_V50(Structure):
    pass

_S(struct_tagNET_DVR_FIBER_CONVERT_BASIC_V50, [
    ('dwSize', DWORD),
    ('byPowerType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwSlotNum', DWORD),
    ('struNetCardInfo', NET_DVR_NETMGR_CARD_INFO_V50),
    ('struFuncCardInfo', NET_DVR_FUNC_CARD_INFO_V50 * 32),
    ('struRemoteSendCardInfo', NET_DVR_REMOTE_SEND_CARD_INFO_V50 * 32),
    ('byRes2', BYTE * 64),
])

NET_DVR_FIBER_CONVERT_BASIC_V50 = struct_tagNET_DVR_FIBER_CONVERT_BASIC_V50
LPNET_DVR_FIBER_CONVERT_BASIC_V50 = POINTER(struct_tagNET_DVR_FIBER_CONVERT_BASIC_V50)
tagNET_DVR_FIBER_CONVERT_BASIC_V50 = struct_tagNET_DVR_FIBER_CONVERT_BASIC_V50
