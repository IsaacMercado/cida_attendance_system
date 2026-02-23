from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_interval_param import NET_ITC_INTERVAL_PARAM
from .net_itc_plate_recog_region_param import NET_ITC_PLATE_RECOG_REGION_PARAM
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_ITC_VTLANE_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_VTLANE_PARAM, [
    ('byRelatedDriveWay', BYTE),
    ('bySpeedCapEn', BYTE),
    ('bySignSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('bySnapTimes', BYTE),
    ('byBigCarSignSpeed', BYTE),
    ('byBigCarSpeedLimit', BYTE),
    ('byRelatedIOOutEx', BYTE),
    ('struInterval', NET_ITC_INTERVAL_PARAM),
    ('byRelatedIOOut', BYTE * 4),
    ('byFlashMode', BYTE),
    ('byLowSpeedLimit', BYTE),
    ('byBigCarLowSpeedLimit', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_REGION_PARAM * 2),
    ('struLine', NET_VCA_LINE),
])

NET_ITC_VTLANE_PARAM = struct_tagNET_ITC_VTLANE_PARAM
LPNET_ITC_VTLANE_PARAM = POINTER(struct_tagNET_ITC_VTLANE_PARAM)
tagNET_ITC_VTLANE_PARAM = struct_tagNET_ITC_VTLANE_PARAM
