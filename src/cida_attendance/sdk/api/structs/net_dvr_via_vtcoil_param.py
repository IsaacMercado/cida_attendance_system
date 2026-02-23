from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_via_lane_param import NET_DVR_VIA_LANE_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM


class struct_tagNET_DVR_VIA_VTCOIL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_VIA_VTCOIL_PARAM, [
    ('byEnable', BYTE),
    ('byLaneNum', BYTE),
    ('byRes', BYTE * 62),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struLaneParam', NET_DVR_VIA_LANE_PARAM * 6),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('byRes1', BYTE * 624),
])

NET_DVR_VIA_VTCOIL_PARAM = struct_tagNET_DVR_VIA_VTCOIL_PARAM
LPNET_DVR_VIA_VTCOIL_PARAM = POINTER(struct_tagNET_DVR_VIA_VTCOIL_PARAM)
tagNET_DVR_VIA_VTCOIL_PARAM = struct_tagNET_DVR_VIA_VTCOIL_PARAM
