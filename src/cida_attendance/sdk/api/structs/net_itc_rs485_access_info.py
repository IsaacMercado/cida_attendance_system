from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_radar_param import NET_ITC_RADAR_PARAM


class struct_tagNET_ITC_RS485_ACCESS_INFO(Structure):
    pass

_S(struct_tagNET_ITC_RS485_ACCESS_INFO, [
    ('dwSize', DWORD),
    ('struRadar', NET_ITC_RADAR_PARAM * 6),
    ('byRes', BYTE * 20),
])

NET_ITC_RS485_ACCESS_INFO = struct_tagNET_ITC_RS485_ACCESS_INFO
LPNET_ITC_RS485_ACCESS_INFO = POINTER(struct_tagNET_ITC_RS485_ACCESS_INFO)
tagNET_ITC_RS485_ACCESS_INFO = struct_tagNET_ITC_RS485_ACCESS_INFO
