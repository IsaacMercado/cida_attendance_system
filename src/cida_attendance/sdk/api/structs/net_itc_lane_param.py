from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_itc_interval_param import NET_ITC_INTERVAL_PARAM
from .net_itc_plate_recog_region_param import NET_ITC_PLATE_RECOG_REGION_PARAM


class struct_tagNET_ITC_LANE_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_PARAM, [
    ('byEnable', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('wDistance', WORD),
    ('wTrigDelayTime', WORD),
    ('byTrigDelayDistance', BYTE),
    ('bySpeedCapEn', BYTE),
    ('bySignSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('bySnapTimes', BYTE),
    ('byOverlayDriveWay', BYTE),
    ('struInterval', NET_ITC_INTERVAL_PARAM),
    ('byRelatedIOOut', BYTE * 4),
    ('byFlashMode', BYTE),
    ('byCartSignSpeed', BYTE),
    ('byCartSpeedLimit', BYTE),
    ('byRelatedIOOutEx', BYTE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_REGION_PARAM * 2),
    ('byLaneType', BYTE),
    ('byUseageType', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('byLowSpeedLimit', BYTE),
    ('byBigCarLowSpeedLimit', BYTE),
    ('byLowSpeedCapEn', BYTE),
    ('byEmergencyCapEn', BYTE),
    ('byRes', BYTE * 9),
])

NET_ITC_LANE_PARAM = struct_tagNET_ITC_LANE_PARAM
LPNET_ITC_LANE_PARAM = POINTER(struct_tagNET_ITC_LANE_PARAM)
tagNET_ITC_LANE_PARAM = struct_tagNET_ITC_LANE_PARAM
