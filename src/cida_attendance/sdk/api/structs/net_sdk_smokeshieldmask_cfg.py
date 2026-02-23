from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_sdk_smokeshieldmask_region import NET_SDK_SMOKESHIELDMASK_REGION


class struct_tagNET_SDK_SMOKESHIELDMASK_CFG(Structure):
    pass

_S(struct_tagNET_SDK_SMOKESHIELDMASK_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byShieldAreaTransparency', BYTE),
    ('byDisplayShieldAreaEnabled', BYTE),
    ('byRes1', BYTE * 1),
    ('struMaskRegion', NET_SDK_SMOKESHIELDMASK_REGION * 24),
    ('byRes', BYTE * 256),
])

NET_SDK_SMOKESHIELDMASK_CFG = struct_tagNET_SDK_SMOKESHIELDMASK_CFG
LPNET_SDK_SMOKESHIELDMASK_CFG = POINTER(struct_tagNET_SDK_SMOKESHIELDMASK_CFG)
tagNET_SDK_SMOKESHIELDMASK_CFG = struct_tagNET_SDK_SMOKESHIELDMASK_CFG
