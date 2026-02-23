from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_interval_param import NET_ITC_INTERVAL_PARAM
from .net_itc_lane_logic_param import NET_ITC_LANE_LOGIC_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_ITC_LANE_HVT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_HVT_PARAM, [
    ('byLaneNO', BYTE),
    ('bySignSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('byBigCarSignSpeed', BYTE),
    ('byBigCarSpeedLimit', BYTE),
    ('bySpeedCapEn', BYTE),
    ('byCaptureCount', BYTE),
    ('byRelatedIOOut', BYTE),
    ('byFlashMode', BYTE),
    ('byEnableRadar', BYTE),
    ('byChangeLaneEnable', BYTE),
    ('byChangeLaneCapNo', BYTE),
    ('dwCapTarget', DWORD),
    ('struInterval', NET_ITC_INTERVAL_PARAM),
    ('byRes3', BYTE * 24),
    ('struLane', NET_ITC_LANE_LOGIC_PARAM),
    ('struLeftLaneLine', NET_ITC_LINE),
    ('struRightLaneLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('struTraceArea', NET_ITC_POLYGON),
    ('struForwardTrigLine', NET_VCA_LINE),
    ('struBackwardTrigLine', NET_VCA_LINE),
    ('struLeftTrigLine', NET_VCA_LINE),
    ('struRightTrigLine', NET_VCA_LINE),
    ('byRes4', BYTE * 60),
])

NET_ITC_LANE_HVT_PARAM = struct_tagNET_ITC_LANE_HVT_PARAM
LPNET_ITC_LANE_HVT_PARAM = POINTER(struct_tagNET_ITC_LANE_HVT_PARAM)
tagNET_ITC_LANE_HVT_PARAM = struct_tagNET_ITC_LANE_HVT_PARAM
