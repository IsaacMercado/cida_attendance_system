from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_aid_info import NET_DVR_AID_INFO
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_AID_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_AID_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struAIDInfo', NET_DVR_AID_INFO),
    ('dwPicDataLen', DWORD),
    ('pImage', POINTER(BYTE)),
    ('byRes', BYTE * 40),
])

NET_DVR_AID_ALARM = struct_tagNET_DVR_AID_ALARM
LPNET_DVR_AID_ALARM = POINTER(struct_tagNET_DVR_AID_ALARM)
tagNET_DVR_AID_ALARM = struct_tagNET_DVR_AID_ALARM
