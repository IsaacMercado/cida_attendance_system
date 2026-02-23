from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_RESULT_(Structure):
    pass

_S(struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_RESULT_, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('dwChannel', DWORD),
    ('dwFlow', DWORD),
    ('byLaneNo', BYTE),
    ('byRes', BYTE * 511),
])

NET_DVR_TRAFFIC_FLOW_QUERY_RESULT = struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_RESULT_
LPNET_DVR_TRAFFIC_FLOW_QUERY_RESULT = POINTER(struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_RESULT_)
tagNET_DVR_TRAFFIC_FLOW_QUERY_RESULT_ = struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_RESULT_
