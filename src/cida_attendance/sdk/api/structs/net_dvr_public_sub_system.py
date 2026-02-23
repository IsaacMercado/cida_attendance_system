from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUBLIC_SUB_SYSTEM(Structure):
    pass

_S(struct_tagNET_DVR_PUBLIC_SUB_SYSTEM, [
    ('dwJointSubSystem', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_PUBLIC_SUB_SYSTEM = struct_tagNET_DVR_PUBLIC_SUB_SYSTEM
LPNET_DVR_PUBLIC_SUB_SYSTEM = POINTER(struct_tagNET_DVR_PUBLIC_SUB_SYSTEM)
tagNET_DVR_PUBLIC_SUB_SYSTEM = struct_tagNET_DVR_PUBLIC_SUB_SYSTEM
