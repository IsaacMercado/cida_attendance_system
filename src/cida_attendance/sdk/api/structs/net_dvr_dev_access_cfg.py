from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEV_ACCESS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DEV_ACCESS_CFG, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wDevicePort', WORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byRes2', BYTE * 60),
])

NET_DVR_DEV_ACCESS_CFG = struct_tagNET_DVR_DEV_ACCESS_CFG
LPNET_DVR_DEV_ACCESS_CFG = POINTER(struct_tagNET_DVR_DEV_ACCESS_CFG)
tagNET_DVR_DEV_ACCESS_CFG = struct_tagNET_DVR_DEV_ACCESS_CFG
