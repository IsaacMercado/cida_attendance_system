from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_TERMINAL_GK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_GK_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRegisterState', BYTE),
    ('byRes1', BYTE * 2),
    ('struGKIP', NET_DVR_IPADDR),
    ('wGKPort', WORD),
    ('byRes2', BYTE * 2),
    ('byRegisterName', BYTE * 64),
    ('byPassword', BYTE * 16),
    ('byRes3', BYTE * 16),
])

NET_DVR_TERMINAL_GK_CFG = struct_tagNET_DVR_TERMINAL_GK_CFG
LPNET_DVR_TERMINAL_GK_CFG = POINTER(struct_tagNET_DVR_TERMINAL_GK_CFG)
tagNET_DVR_TERMINAL_GK_CFG = struct_tagNET_DVR_TERMINAL_GK_CFG
