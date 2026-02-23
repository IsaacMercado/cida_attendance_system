from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_POS_OSD_REGION(Structure):
    pass

_S(struct_tagNET_DVR_POS_OSD_REGION, [
    ('struStart', NET_VCA_POINT),
    ('struEnd', NET_VCA_POINT),
])

NET_DVR_POS_OSD_REGION = struct_tagNET_DVR_POS_OSD_REGION
LPNET_DVR_POS_OSD_REGION = POINTER(struct_tagNET_DVR_POS_OSD_REGION)
tagNET_DVR_POS_OSD_REGION = struct_tagNET_DVR_POS_OSD_REGION
