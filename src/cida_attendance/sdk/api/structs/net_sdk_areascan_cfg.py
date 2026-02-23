from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_SDK_AREASCAN_CFG(Structure):
    pass

_S(struct_tagNET_SDK_AREASCAN_CFG, [
    ('dwSize', DWORD),
    ('byScanState', BYTE),
    ('byRes', BYTE * 259),
])

NET_SDK_AREASCAN_CFG = struct_tagNET_SDK_AREASCAN_CFG
LPNET_SDK_AREASCAN_CFG = POINTER(struct_tagNET_SDK_AREASCAN_CFG)
tagNET_SDK_AREASCAN_CFG = struct_tagNET_SDK_AREASCAN_CFG
