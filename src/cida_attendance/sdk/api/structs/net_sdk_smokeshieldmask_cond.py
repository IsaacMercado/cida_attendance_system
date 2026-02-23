from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_SDK_SMOKESHIELDMASK_COND(Structure):
    pass

_S(struct_tagNET_SDK_SMOKESHIELDMASK_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRegionID', BYTE),
    ('byRes', BYTE * 127),
])

NET_SDK_SMOKESHIELDMASK_COND = struct_tagNET_SDK_SMOKESHIELDMASK_COND
LPNET_SDK_SMOKESHIELDMASK_COND = POINTER(struct_tagNET_SDK_SMOKESHIELDMASK_COND)
tagNET_SDK_SMOKESHIELDMASK_COND = struct_tagNET_SDK_SMOKESHIELDMASK_COND
