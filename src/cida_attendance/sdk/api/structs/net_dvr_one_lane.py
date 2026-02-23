from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_direction import NET_DVR_DIRECTION
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_ONE_LANE(Structure):
    pass

_S(struct_tagNET_DVR_ONE_LANE, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 11),
    ('byLaneName', BYTE * 32),
    ('struFlowDirection', NET_DVR_DIRECTION),
    ('struPolygon', NET_VCA_POLYGON),
])

NET_DVR_ONE_LANE = struct_tagNET_DVR_ONE_LANE
LPNET_DVR_ONE_LANE = POINTER(struct_tagNET_DVR_ONE_LANE)
tagNET_DVR_ONE_LANE = struct_tagNET_DVR_ONE_LANE
