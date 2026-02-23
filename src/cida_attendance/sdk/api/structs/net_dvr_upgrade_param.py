from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_UPGRADE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_UPGRADE_PARAM, [
    ('dwUpgradeType', DWORD),
    ('sFileName', String),
    ('pInbuffer', POINTER(None)),
    ('dwBufferLen', DWORD),
    ('pUnitIdList', POINTER(c_char) * 64),
    ('byRes', BYTE * 112),
])

NET_DVR_UPGRADE_PARAM = struct_tagNET_DVR_UPGRADE_PARAM
LPNET_DVR_UPGRADE_PARAM = POINTER(struct_tagNET_DVR_UPGRADE_PARAM)
tagNET_DVR_UPGRADE_PARAM = struct_tagNET_DVR_UPGRADE_PARAM
