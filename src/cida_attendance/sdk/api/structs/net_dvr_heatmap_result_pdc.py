from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_single_heatmap_result_pdc import NET_DVR_SINGLE_HEATMAP_RESULT_PDC
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_HEATMAP_RESULT_PDC(Structure):
    pass

_S(struct_tagNET_DVR_HEATMAP_RESULT_PDC, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byBrokenNetHttp', BYTE),
    ('byArrayUnitType', BYTE),
    ('struSingleHeatMap', NET_DVR_SINGLE_HEATMAP_RESULT_PDC * 2),
    ('wCurNumber', WORD),
    ('wLeaveNumber', WORD),
    ('pEventNotificationAlertBuff', String),
    ('dwEventNotificationAlertLen', DWORD),
    ('byRes1', BYTE * 48),
])

NET_DVR_HEATMAP_RESULT_PDC = struct_tagNET_DVR_HEATMAP_RESULT_PDC
LPNET_DVR_HEATMAP_RESULT_PDC = POINTER(struct_tagNET_DVR_HEATMAP_RESULT_PDC)
tagNET_DVR_HEATMAP_RESULT_PDC = struct_tagNET_DVR_HEATMAP_RESULT_PDC
