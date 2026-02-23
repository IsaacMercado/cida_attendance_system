from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_TARGET_LEFT_REGION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_TARGET_LEFT_REGION_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('byTargetType', BYTE),
    ('byLeftDirection', BYTE),
    ('byTargetStatus', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_TARGET_LEFT_REGION_ALARM = struct_tagNET_DVR_TARGET_LEFT_REGION_ALARM
LPNET_DVR_TARGET_LEFT_REGION_ALARM = POINTER(struct_tagNET_DVR_TARGET_LEFT_REGION_ALARM)
tagNET_DVR_TARGET_LEFT_REGION_ALARM = struct_tagNET_DVR_TARGET_LEFT_REGION_ALARM
