from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_bonding import NET_DVR_ONE_BONDING


class struct_tagNET_DVR_NETWORK_BONDING(Structure):
    pass

_S(struct_tagNET_DVR_NETWORK_BONDING, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byNum', BYTE),
    ('byRes1', BYTE * 2),
    ('struOneBond', NET_DVR_ONE_BONDING * 2),
    ('byRes2', BYTE * 40),
])

NET_DVR_NETWORK_BONDING = struct_tagNET_DVR_NETWORK_BONDING
LPNET_DVR_NETWORK_BONDING = POINTER(struct_tagNET_DVR_NETWORK_BONDING)
tagNET_DVR_NETWORK_BONDING = struct_tagNET_DVR_NETWORK_BONDING
