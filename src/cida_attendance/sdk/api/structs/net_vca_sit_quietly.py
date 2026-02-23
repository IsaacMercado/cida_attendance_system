from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_SIT_QUIETLY(Structure):
    pass

_S(struct_tagNET_VCA_SIT_QUIETLY, [
    ('struRegion', NET_VCA_POLYGON),
    ('dwDuration', DWORD),
    ('byRes', BYTE * 4),
])

NET_VCA_SIT_QUIETLY = struct_tagNET_VCA_SIT_QUIETLY
LPNET_VCA_SIT_QUIETLY = POINTER(struct_tagNET_VCA_SIT_QUIETLY)
tagNET_VCA_SIT_QUIETLY = struct_tagNET_VCA_SIT_QUIETLY
