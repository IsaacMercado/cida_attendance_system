from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WEP_KEY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WEP_KEY_CFG, [
    ('csWEPKey', c_char * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_WEP_KEY_CFG = struct_tagNET_DVR_WEP_KEY_CFG
LPNET_DVR_WEP_KEY_CFG = POINTER(struct_tagNET_DVR_WEP_KEY_CFG)
tagNET_DVR_WEP_KEY_CFG = struct_tagNET_DVR_WEP_KEY_CFG
