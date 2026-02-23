from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_NOSIGNAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_NOSIGNAL_CFG, [
    ('dwSize', DWORD),
    ('byNoSignalMode', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_LED_NOSIGNAL_CFG = struct_tagNET_DVR_LED_NOSIGNAL_CFG
LPNET_DVR_LED_NOSIGNAL_CFG = POINTER(struct_tagNET_DVR_LED_NOSIGNAL_CFG)
tagNET_DVR_LED_NOSIGNAL_CFG = struct_tagNET_DVR_LED_NOSIGNAL_CFG
