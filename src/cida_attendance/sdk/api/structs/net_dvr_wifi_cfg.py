from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_wifi_cfg_ex import NET_DVR_WIFI_CFG_EX


class struct_tagNET_DVR_WIFI_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIFI_CFG, [
    ('dwSize', DWORD),
    ('struWifiCfg', NET_DVR_WIFI_CFG_EX),
])

NET_DVR_WIFI_CFG = struct_tagNET_DVR_WIFI_CFG
LPNET_DVR_WIFI_CFG = POINTER(struct_tagNET_DVR_WIFI_CFG)
tagNET_DVR_WIFI_CFG = struct_tagNET_DVR_WIFI_CFG
