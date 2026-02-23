from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_tps_info_v41 import NET_DVR_TPS_INFO_V41
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_TPS_ALARM_V41(Structure):
    pass

_S(struct_tagNET_DVR_TPS_ALARM_V41, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struTPSInfo', NET_DVR_TPS_INFO_V41),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('dwStartTime', DWORD),
    ('dwStopTime', DWORD),
    ('byRes', BYTE * 24),
])

NET_DVR_TPS_ALARM_V41 = struct_tagNET_DVR_TPS_ALARM_V41
LPNET_DVR_TPS_ALARM_V41 = POINTER(struct_tagNET_DVR_TPS_ALARM_V41)
tagNET_DVR_TPS_ALARM_V41 = struct_tagNET_DVR_TPS_ALARM_V41
