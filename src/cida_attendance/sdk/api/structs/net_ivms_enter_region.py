from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_enter_region import NET_VCA_ENTER_REGION


class struct_tagNET_IVMS_ENTER_REGION(Structure):
    pass

_S(struct_tagNET_IVMS_ENTER_REGION, [
    ('dwSize', DWORD),
    ('struEnter', (NET_VCA_ENTER_REGION * 4) * 7),
])

NET_IVMS_ENTER_REGION = struct_tagNET_IVMS_ENTER_REGION
LPNET_IVMS_ENTER_REGION = POINTER(struct_tagNET_IVMS_ENTER_REGION)
tagNET_IVMS_ENTER_REGION = struct_tagNET_IVMS_ENTER_REGION
