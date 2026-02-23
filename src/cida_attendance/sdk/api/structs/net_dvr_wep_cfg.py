from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_wep_key_cfg import NET_DVR_WEP_KEY_CFG


class struct_tagNET_DVR_WEP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WEP_CFG, [
    ('byAuthenticationType', BYTE),
    ('byDefaultTransmitKeyIndex', BYTE),
    ('byWepKeyLenType', BYTE),
    ('byKeyType', BYTE),
    ('struWEPKeyCfg', NET_DVR_WEP_KEY_CFG * 4),
    ('byRes', BYTE * 128),
])

NET_DVR_WEP_CFG = struct_tagNET_DVR_WEP_CFG
LPNET_DVR_WEP_CFG = POINTER(struct_tagNET_DVR_WEP_CFG)
tagNET_DVR_WEP_CFG = struct_tagNET_DVR_WEP_CFG
