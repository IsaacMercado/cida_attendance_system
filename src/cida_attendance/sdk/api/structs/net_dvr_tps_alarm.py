from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_tps_info import NET_DVR_TPS_INFO
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_TPS_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_TPS_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struTPSInfo', NET_DVR_TPS_INFO),
    ('byRes1', BYTE * 32),
])

NET_DVR_TPS_ALARM = struct_tagNET_DVR_TPS_ALARM
LPNET_DVR_TPS_ALARM = POINTER(struct_tagNET_DVR_TPS_ALARM)
tagNET_DVR_TPS_ALARM = struct_tagNET_DVR_TPS_ALARM
