from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_wep_cfg import NET_DVR_WEP_CFG
from .net_dvr_wpa_cfg import NET_DVR_WPA_CFG


class struct_tagNET_DVR_WIRELESS_SECURITY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIRELESS_SECURITY_CFG, [
    ('bySecurityMode', BYTE),
    ('struWEPCfg', NET_DVR_WEP_CFG),
    ('struWPACfg', NET_DVR_WPA_CFG),
    ('byRes', BYTE * 256),
])

NET_DVR_WIRELESS_SECURITY_CFG = struct_tagNET_DVR_WIRELESS_SECURITY_CFG
LPNET_DVR_WIRELESS_SECURITY_CFG = POINTER(struct_tagNET_DVR_WIRELESS_SECURITY_CFG)
tagNET_DVR_WIRELESS_SECURITY_CFG = struct_tagNET_DVR_WIRELESS_SECURITY_CFG
