from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_PASSWD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CARD_PASSWD_CFG, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardPassword', BYTE * 8),
    ('dwErrorCode', DWORD),
    ('byCardValid', BYTE),
    ('byRes2', BYTE * 23),
])

NET_DVR_CARD_PASSWD_CFG = struct_tagNET_DVR_CARD_PASSWD_CFG
LPNET_DVR_CARD_PASSWD_CFG = POINTER(struct_tagNET_DVR_CARD_PASSWD_CFG)
tagNET_DVR_CARD_PASSWD_CFG = struct_tagNET_DVR_CARD_PASSWD_CFG
