from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_SDK_FIRESHIELDMASK_COND(Structure):
    pass

_S(struct_tagNET_SDK_FIRESHIELDMASK_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRegionID', BYTE),
    ('byRes', BYTE * 127),
])

NET_SDK_FIRESHIELDMASK_COND = struct_tagNET_SDK_FIRESHIELDMASK_COND
LPNET_SDK_FIRESHIELDMASK_COND = POINTER(struct_tagNET_SDK_FIRESHIELDMASK_COND)
tagNET_SDK_FIRESHIELDMASK_COND = struct_tagNET_SDK_FIRESHIELDMASK_COND
