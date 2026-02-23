from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_HEATMAP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_HEATMAP_INFO, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('dwHeatMapPicLen', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwTimeHeatMapValue', DWORD),
    ('dwHeatMapMaxValue', DWORD),
    ('dwHeatMapMinValue', DWORD),
    ('wArrayLine', WORD),
    ('wArrayColumn', WORD),
    ('pArrayBuffer', POINTER(BYTE)),
    ('byArrayUnitType', BYTE),
    ('byRes', BYTE * 107),
])

NET_DVR_HEATMAP_INFO = struct_tagNET_DVR_HEATMAP_INFO
LPNET_DVR_HEATMAP_INFO = POINTER(struct_tagNET_DVR_HEATMAP_INFO)
tagNET_DVR_HEATMAP_INFO = struct_tagNET_DVR_HEATMAP_INFO
