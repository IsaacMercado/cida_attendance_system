from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_interval_param import NET_ITC_INTERVAL_PARAM
from .net_itc_lane_logic_param import NET_ITC_LANE_LOGIC_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_ITC_LANE_HVT_PARAM_V50(Structure):
    pass

_S(struct_tagNET_ITC_LANE_HVT_PARAM_V50, [
    ('byLaneNO', BYTE),
    ('byFlashMode', BYTE),
    ('bySignSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('bySignLowSpeed', BYTE),
    ('byLowSpeedLimit', BYTE),
    ('byBigCarSignSpeed', BYTE),
    ('byBigCarSpeedLimit', BYTE),
    ('byBigCarSignLowSpeed', BYTE),
    ('byBigCarLowSpeedLimit', BYTE),
    ('bySnapTimes', BYTE),
    ('byDriveLineSnapTime', BYTE),
    ('byHighSpeedSnapTime', BYTE),
    ('byLowSpeedSnapTime', BYTE),
    ('byBanSnapTime', BYTE),
    ('byReverseSnapTime', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('byLaneType', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('byRes1', BYTE * 27),
    ('byChangeLaneEnable', BYTE),
    ('byChangeLaneCapNo', BYTE),
    ('dwVioDetectType', DWORD),
    ('dwRelatedIOOut', DWORD),
    ('struTrigLine', NET_ITC_LINE),
    ('struLineLeft', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('struLane', NET_ITC_LANE_LOGIC_PARAM),
    ('struInterval', NET_ITC_INTERVAL_PARAM),
    ('byRes2', BYTE * 280),
])

NET_ITC_LANE_HVT_PARAM_V50 = struct_tagNET_ITC_LANE_HVT_PARAM_V50
LPNET_ITC_LANE_HVT_PARAM_V50 = POINTER(struct_tagNET_ITC_LANE_HVT_PARAM_V50)
tagNET_ITC_LANE_HVT_PARAM_V50 = struct_tagNET_ITC_LANE_HVT_PARAM_V50
