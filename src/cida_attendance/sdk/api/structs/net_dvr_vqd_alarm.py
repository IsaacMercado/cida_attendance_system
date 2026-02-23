from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_VQD_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_VQD_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwEventType', DWORD),
    ('fThreshold', c_float),
    ('dwPicDataLen', DWORD),
    ('pImage', POINTER(BYTE)),
    ('byRes', BYTE * 128),
])

NET_DVR_VQD_ALARM = struct_tagNET_DVR_VQD_ALARM
LPNET_DVR_VQD_ALARM = POINTER(struct_tagNET_DVR_VQD_ALARM)
tagNET_DVR_VQD_ALARM = struct_tagNET_DVR_VQD_ALARM
