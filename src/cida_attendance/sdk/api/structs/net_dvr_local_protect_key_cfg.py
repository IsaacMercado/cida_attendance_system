from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_PROTECT_KEY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_PROTECT_KEY_CFG, [
    ('byProtectKey', BYTE * 128),
    ('byRes', BYTE * 128),
])

NET_DVR_LOCAL_PROTECT_KEY_CFG = struct_tagNET_DVR_LOCAL_PROTECT_KEY_CFG
LPNET_DVR_LOCAL_PROTECT_KEY_CFG = POINTER(struct_tagNET_DVR_LOCAL_PROTECT_KEY_CFG)
tagNET_DVR_LOCAL_PROTECT_KEY_CFG = struct_tagNET_DVR_LOCAL_PROTECT_KEY_CFG
