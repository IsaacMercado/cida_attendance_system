from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_USER_INFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CARD_USER_INFO_CFG, [
    ('dwSize', DWORD),
    ('sUsername', BYTE * 32),
    ('byAssociateNetUser', BYTE),
    ('byRes2', BYTE * 255),
])

NET_DVR_CARD_USER_INFO_CFG = struct_tagNET_DVR_CARD_USER_INFO_CFG
LPNET_DVR_CARD_USER_INFO_CFG = POINTER(struct_tagNET_DVR_CARD_USER_INFO_CFG)
tagNET_DVR_CARD_USER_INFO_CFG = struct_tagNET_DVR_CARD_USER_INFO_CFG
