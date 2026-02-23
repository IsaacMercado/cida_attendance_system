from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_452 import union_anon_452


class struct_tagNET_DVR_IPDEVICE_ACTIVATE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_IPDEVICE_ACTIVATE_CFG, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('bySelfDefinePassword', BYTE),
    ('sPassword', BYTE * 16),
    ('sUserName', BYTE * 32),
    ('byRes', BYTE * 78),
    ('unActivateDeviceInfo', union_anon_452),
])

NET_DVR_IPDEVICE_ACTIVATE_CFG = struct_tagNET_DVR_IPDEVICE_ACTIVATE_CFG
LPNET_DVR_IPDEVICE_ACTIVATE_CFG = POINTER(struct_tagNET_DVR_IPDEVICE_ACTIVATE_CFG)
tagNET_DVR_IPDEVICE_ACTIVATE_CFG = struct_tagNET_DVR_IPDEVICE_ACTIVATE_CFG
