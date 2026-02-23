from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_SDK_FIRESHIELDMASK_REGION(Structure):
    pass

_S(struct_tagNET_SDK_FIRESHIELDMASK_REGION, [
    ('dwSize', DWORD),
    ('byMaskID', BYTE),
    ('byEnabled', BYTE),
    ('byShieldZoom', BYTE),
    ('byMaskType', BYTE),
    ('byRegionType', BYTE),
    ('byShowEnabled', BYTE),
    ('byRes1', BYTE * 2),
    ('szMaskName', c_char * 32),
    ('struRegion', NET_VCA_POLYGON),
    ('byRes', BYTE * 32),
])

NET_SDK_FIRESHIELDMASK_REGION = struct_tagNET_SDK_FIRESHIELDMASK_REGION
LPNET_SDK_FIRESHIELDMASK_REGION = POINTER(struct_tagNET_SDK_FIRESHIELDMASK_REGION)
tagNET_SDK_FIRESHIELDMASK_REGION = struct_tagNET_SDK_FIRESHIELDMASK_REGION
