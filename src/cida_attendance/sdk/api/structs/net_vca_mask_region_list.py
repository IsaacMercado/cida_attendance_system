from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_mask_region import NET_VCA_MASK_REGION


class struct_tagNET_VCA_MASK_REGION_LIST(Structure):
    pass

_S(struct_tagNET_VCA_MASK_REGION_LIST, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 4),
    ('struMask', NET_VCA_MASK_REGION * 4),
])

NET_VCA_MASK_REGION_LIST = struct_tagNET_VCA_MASK_REGION_LIST
LPNET_VCA_MASK_REGION_LIST = POINTER(struct_tagNET_VCA_MASK_REGION_LIST)
tagNET_VCA_MASK_REGION_LIST = struct_tagNET_VCA_MASK_REGION_LIST
