from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_sdk_fireshieldmask_region import NET_SDK_FIRESHIELDMASK_REGION


class struct_tagNET_SDK_FIRESHIELDMASK_CFG(Structure):
    pass

_S(struct_tagNET_SDK_FIRESHIELDMASK_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byShieldAreaTransparency', BYTE),
    ('byDisplayShieldAreaEnabled', BYTE),
    ('byRes1', BYTE * 1),
    ('struMaskRegion', NET_SDK_FIRESHIELDMASK_REGION * 24),
    ('byRes', BYTE * 256),
])

NET_SDK_FIRESHIELDMASK_CFG = struct_tagNET_SDK_FIRESHIELDMASK_CFG
LPNET_SDK_FIRESHIELDMASK_CFG = POINTER(struct_tagNET_SDK_FIRESHIELDMASK_CFG)
tagNET_SDK_FIRESHIELDMASK_CFG = struct_tagNET_SDK_FIRESHIELDMASK_CFG
