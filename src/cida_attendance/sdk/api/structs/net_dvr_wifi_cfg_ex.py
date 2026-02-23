from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_214 import union_anon_214
from .net_dvr_wifiethernet import NET_DVR_WIFIETHERNET


class struct_tagNET_DVR_WIFI_CFG_EX(Structure):
    pass

_S(struct_tagNET_DVR_WIFI_CFG_EX, [
    ('struEtherNet', NET_DVR_WIFIETHERNET),
    ('sEssid', c_char * 32),
    ('dwMode', DWORD),
    ('dwSecurity', DWORD),
    ('key', union_anon_214),
])

NET_DVR_WIFI_CFG_EX = struct_tagNET_DVR_WIFI_CFG_EX
LPNET_DVR_WIFI_CFG_EX = POINTER(struct_tagNET_DVR_WIFI_CFG_EX)
tagNET_DVR_WIFI_CFG_EX = struct_tagNET_DVR_WIFI_CFG_EX
