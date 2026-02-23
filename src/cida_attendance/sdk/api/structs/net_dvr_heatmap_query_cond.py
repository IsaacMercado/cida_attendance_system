from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_HEATMAP_QUERY_COND(Structure):
    pass

_S(struct_tagNET_DVR_HEATMAP_QUERY_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byReportType', BYTE),
    ('byDetSceneID', BYTE),
    ('byHeatMapInfoType', BYTE),
    ('byStatisticalModel', BYTE),
    ('byRes', BYTE * 124),
])

NET_DVR_HEATMAP_QUERY_COND = struct_tagNET_DVR_HEATMAP_QUERY_COND
LPNET_DVR_HEATMAP_QUERY_COND = POINTER(struct_tagNET_DVR_HEATMAP_QUERY_COND)
tagNET_DVR_HEATMAP_QUERY_COND = struct_tagNET_DVR_HEATMAP_QUERY_COND
