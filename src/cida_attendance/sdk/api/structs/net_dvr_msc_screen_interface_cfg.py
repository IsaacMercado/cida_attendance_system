from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MSC_SCREEN_INTERFACE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MSC_SCREEN_INTERFACE_CFG, [
    ('dwSize', DWORD),
    ('byInterfaceType', BYTE),
    ('byNoSignalPic', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_MSC_SCREEN_INTERFACE_CFG = struct_tagNET_DVR_MSC_SCREEN_INTERFACE_CFG
LPNET_DVR_MSC_SCREEN_INTERFACE_CFG = POINTER(struct_tagNET_DVR_MSC_SCREEN_INTERFACE_CFG)
tagNET_DVR_MSC_SCREEN_INTERFACE_CFG = struct_tagNET_DVR_MSC_SCREEN_INTERFACE_CFG
