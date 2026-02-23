from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_CONNECTDEV_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CONNECTDEV_CFG, [
    ('dwSize', DWORD),
    ('byID', BYTE),
    ('byRes', BYTE * 1),
    ('byMACAddr', BYTE * 6),
    ('struDVRIP', NET_DVR_IPADDR),
    ('struConnectTime', NET_DVR_TIME),
    ('byRes1', BYTE * 256),
])

NET_DVR_CONNECTDEV_CFG = struct_tagNET_DVR_CONNECTDEV_CFG
LPNET_DVR_CONNECTDEV_CFG = POINTER(struct_tagNET_DVR_CONNECTDEV_CFG)
tagNET_DVR_CONNECTDEV_CFG = struct_tagNET_DVR_CONNECTDEV_CFG
