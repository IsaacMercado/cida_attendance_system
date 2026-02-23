from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_VANDALPROOF_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_VANDALPROOF_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('byRes', BYTE * 256),
])

NET_DVR_VANDALPROOF_ALARM = struct_tagNET_DVR_VANDALPROOF_ALARM
LPNET_DVR_VANDALPROOF_ALARM = POINTER(struct_tagNET_DVR_VANDALPROOF_ALARM)
tagNET_DVR_VANDALPROOF_ALARM = struct_tagNET_DVR_VANDALPROOF_ALARM
