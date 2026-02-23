from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_access_devinfo_param_union import NET_ITC_ACCESS_DEVINFO_PARAM_UNION


class struct_tagNET_ITC_RS485_ACCESS_CFG(Structure):
    pass

_S(struct_tagNET_ITC_RS485_ACCESS_CFG, [
    ('dwSize', DWORD),
    ('byModeType', BYTE),
    ('byRes', BYTE * 3),
    ('uITCAccessDevinfoParam', NET_ITC_ACCESS_DEVINFO_PARAM_UNION),
    ('byRes1', BYTE * 12),
])

NET_ITC_RS485_ACCESS_CFG = struct_tagNET_ITC_RS485_ACCESS_CFG
LPNET_ITC_RS485_ACCESS_CFG = POINTER(struct_tagNET_ITC_RS485_ACCESS_CFG)
tagNET_ITC_RS485_ACCESS_CFG = struct_tagNET_ITC_RS485_ACCESS_CFG
