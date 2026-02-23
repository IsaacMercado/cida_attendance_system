from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FUZZY_UPGRADE(Structure):
    pass

_S(struct_tagNET_DVR_FUZZY_UPGRADE, [
    ('dwSize', DWORD),
    ('sUpgradeInfo', c_char * 48),
    ('byRes', BYTE * 64),
])

NET_DVR_FUZZY_UPGRADE = struct_tagNET_DVR_FUZZY_UPGRADE
LPNET_DVR_FUZZY_UPGRADE = POINTER(struct_tagNET_DVR_FUZZY_UPGRADE)
tagNET_DVR_FUZZY_UPGRADE = struct_tagNET_DVR_FUZZY_UPGRADE
