from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_VCA_SINGLE_FACESNAPCFG(Structure):
    pass

_S(struct_tagNET_VCA_SINGLE_FACESNAPCFG, [
    ('byActive', BYTE),
    ('byAutoROIEnable', BYTE),
    ('byRes', BYTE * 2),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struVcaPolygon', NET_VCA_POLYGON),
])

NET_VCA_SINGLE_FACESNAPCFG = struct_tagNET_VCA_SINGLE_FACESNAPCFG
LPNET_VCA_SINGLE_FACESNAPCFG = POINTER(struct_tagNET_VCA_SINGLE_FACESNAPCFG)
tagNET_VCA_SINGLE_FACESNAPCFG = struct_tagNET_VCA_SINGLE_FACESNAPCFG
