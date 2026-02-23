from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_func_card_info import NET_DVR_FUNC_CARD_INFO
from .net_dvr_netmgr_card_info import NET_DVR_NETMGR_CARD_INFO


class struct_tagNET_DVR_FIBER_CONVERT_BASIC(Structure):
    pass

_S(struct_tagNET_DVR_FIBER_CONVERT_BASIC, [
    ('dwSize', DWORD),
    ('byPowerType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwSlotNum', DWORD),
    ('struNetCardInfo', NET_DVR_NETMGR_CARD_INFO),
    ('struFuncCardInfo', NET_DVR_FUNC_CARD_INFO * 32),
    ('byRes2', BYTE * 64),
])

NET_DVR_FIBER_CONVERT_BASIC = struct_tagNET_DVR_FIBER_CONVERT_BASIC
LPNET_DVR_FIBER_CONVERT_BASIC = POINTER(struct_tagNET_DVR_FIBER_CONVERT_BASIC)
tagNET_DVR_FIBER_CONVERT_BASIC = struct_tagNET_DVR_FIBER_CONVERT_BASIC
