from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_DENSEFOGDETECTION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_DENSEFOGDETECTION_ALARM, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byFogLevel', BYTE),
    ('byRes', BYTE * 259),
])

NET_DVR_DENSEFOGDETECTION_ALARM = struct_tagNET_DVR_DENSEFOGDETECTION_ALARM
LPNET_DVR_DENSEFOGDETECTION_ALARM = POINTER(struct_tagNET_DVR_DENSEFOGDETECTION_ALARM)
tagNET_DVR_DENSEFOGDETECTION_ALARM = struct_tagNET_DVR_DENSEFOGDETECTION_ALARM
