from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BONJOUR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BONJOUR_CFG, [
    ('dwSize', DWORD),
    ('byEnableBonjour', BYTE),
    ('byRes1', BYTE * 3),
    ('byFriendlyName', BYTE * 64),
    ('byRes2', BYTE * 128),
])

NET_DVR_BONJOUR_CFG = struct_tagNET_DVR_BONJOUR_CFG
LPNET_DVR_BONJOUR_CFG = POINTER(struct_tagNET_DVR_BONJOUR_CFG)
tagNET_DVR_BONJOUR_CFG = struct_tagNET_DVR_BONJOUR_CFG
