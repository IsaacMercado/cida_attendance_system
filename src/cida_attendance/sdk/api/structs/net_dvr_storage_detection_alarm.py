from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_STORAGE_DETECTION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_STORAGE_DETECTION_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwCardID', DWORD),
    ('wAbnormalPowerLoss', WORD),
    ('wBadBlocks', WORD),
    ('byHealthState', BYTE),
    ('byRes1', BYTE * 3),
    ('fResidualLife', c_float),
    ('byRes', BYTE * 118),
])

NET_DVR_STORAGE_DETECTION_ALARM = struct_tagNET_DVR_STORAGE_DETECTION_ALARM
LPNET_DVR_STORAGE_DETECTION_ALARM = POINTER(struct_tagNET_DVR_STORAGE_DETECTION_ALARM)
tagNET_DVR_STORAGE_DETECTION_ALARM = struct_tagNET_DVR_STORAGE_DETECTION_ALARM
