from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_COND_(Structure):
    pass

_S(struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_COND_, [
    ('dwSize', DWORD),
    ('dwQueryCond', DWORD),
    ('dwChannel', DWORD),
    ('dwResChan', DWORD * 10),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byLaneNo', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_TRAFFIC_FLOW_QUERY_COND = struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_COND_
LPNET_DVR_TRAFFIC_FLOW_QUERY_COND = POINTER(struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_COND_)
tagNET_DVR_TRAFFIC_FLOW_QUERY_COND_ = struct_tagNET_DVR_TRAFFIC_FLOW_QUERY_COND_
