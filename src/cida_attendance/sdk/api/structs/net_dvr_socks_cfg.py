from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SOCKS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SOCKS_CFG, [
    ('dwSize', DWORD),
    ('byEnableSocks', BYTE),
    ('byVersion', BYTE),
    ('wProxyPort', WORD),
    ('byProxyaddr', BYTE * 64),
    ('byUserName', BYTE * 64),
    ('byPassword', BYTE * 32),
    ('byLocalAddr', BYTE * 96),
    ('byRes', BYTE * 128),
])

NET_DVR_SOCKS_CFG = struct_tagNET_DVR_SOCKS_CFG
LPNET_DVR_SOCKS_CFG = POINTER(struct_tagNET_DVR_SOCKS_CFG)
tagNET_DVR_SOCKS_CFG = struct_tagNET_DVR_SOCKS_CFG
