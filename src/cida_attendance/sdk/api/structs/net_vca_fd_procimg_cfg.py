from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_fd_image_cfg import NET_VCA_FD_IMAGE_CFG
from .net_vca_polygon import NET_VCA_POLYGON
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_VCA_FD_PROCIMG_CFG(Structure):
    pass

_S(struct_tagNET_VCA_FD_PROCIMG_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySensitivity', BYTE),
    ('byRes1', BYTE * 22),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struPolygon', NET_VCA_POLYGON),
    ('struFDImage', NET_VCA_FD_IMAGE_CFG),
    ('byRes2', BYTE * 20),
])

NET_VCA_FD_PROCIMG_CFG = struct_tagNET_VCA_FD_PROCIMG_CFG
LPNET_VCA_FD_PROCIMG_CFG = POINTER(struct_tagNET_VCA_FD_PROCIMG_CFG)
tagNET_VCA_FD_PROCIMG_CFG = struct_tagNET_VCA_FD_PROCIMG_CFG
