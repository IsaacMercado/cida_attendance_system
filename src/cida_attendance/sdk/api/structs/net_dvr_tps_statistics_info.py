from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_tps_statistics_param import NET_DVR_TPS_STATISTICS_PARAM


class struct_tagNET_DVR_TPS_STATISTICS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_TPS_STATISTICS_INFO, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('struTPSStatisticsInfo', NET_DVR_TPS_STATISTICS_PARAM),
    ('dwJsonLen', DWORD),
    ('pJsonBuf', POINTER(BYTE)),
    ('byJsonInfoFlag', BYTE),
    ('byBrokenNetHttp', BYTE),
    ('byRes', BYTE * 114),
])

NET_DVR_TPS_STATISTICS_INFO = struct_tagNET_DVR_TPS_STATISTICS_INFO
LPNET_DVR_TPS_STATISTICS_INFO = POINTER(struct_tagNET_DVR_TPS_STATISTICS_INFO)
tagNET_DVR_TPS_STATISTICS_INFO = struct_tagNET_DVR_TPS_STATISTICS_INFO
