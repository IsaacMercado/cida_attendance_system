from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_HEATMAP_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_HEATMAP_RESULT, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('dwMaxHeatMapValue', DWORD),
    ('dwMinHeatMapValue', DWORD),
    ('dwTimeHeatMapValue', DWORD),
    ('wArrayLine', WORD),
    ('wArrayColumn', WORD),
    ('pBuffer', POINTER(BYTE)),
    ('byDetSceneID', BYTE),
    ('byBrokenNetHttp', BYTE),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byTimeDiffFlag', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byArrayUnitType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwTotalTime', DWORD),
    ('byRes', BYTE * 112),
])

NET_DVR_HEATMAP_RESULT = struct_tagNET_DVR_HEATMAP_RESULT
LPNET_DVR_HEATMAP_RESULT = POINTER(struct_tagNET_DVR_HEATMAP_RESULT)
tagNET_DVR_HEATMAP_RESULT = struct_tagNET_DVR_HEATMAP_RESULT
