from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_interval_param import NET_ITC_INTERVAL_PARAM
from .net_itc_lane_logic_param import NET_ITC_LANE_LOGIC_PARAM
from .net_itc_polygon import NET_ITC_POLYGON
from .net_itc_violation_detect_line import NET_ITC_VIOLATION_DETECT_LINE
from .net_itc_violation_detect_param import NET_ITC_VIOLATION_DETECT_PARAM


class struct_tagNET_ITC_LANE_VIDEO_EPOLICE_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_VIDEO_EPOLICE_PARAM, [
    ('byLaneNO', BYTE),
    ('bySensitivity', BYTE),
    ('byEnableRadar', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('struLane', NET_ITC_LANE_LOGIC_PARAM),
    ('struVioDetect', NET_ITC_VIOLATION_DETECT_PARAM),
    ('struLine', NET_ITC_VIOLATION_DETECT_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('byRecordEnable', BYTE),
    ('byRecordType', BYTE),
    ('byPreRecordTime', BYTE),
    ('byRecordDelayTime', BYTE),
    ('byRecordTimeOut', BYTE),
    ('byCarSpeedLimit', BYTE),
    ('byCarSignSpeed', BYTE),
    ('bySnapPicPreRecord', BYTE),
    ('struInterval', NET_ITC_INTERVAL_PARAM),
    ('byRes', BYTE * 36),
])

NET_ITC_LANE_VIDEO_EPOLICE_PARAM = struct_tagNET_ITC_LANE_VIDEO_EPOLICE_PARAM
LPNET_ITC_LANE_VIDEO_EPOLICE_PARAM = POINTER(struct_tagNET_ITC_LANE_VIDEO_EPOLICE_PARAM)
tagNET_ITC_LANE_VIDEO_EPOLICE_PARAM = struct_tagNET_ITC_LANE_VIDEO_EPOLICE_PARAM
