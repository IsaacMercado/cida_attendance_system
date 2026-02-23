from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_SWITCH_LAMP_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_SWITCH_LAMP_ALARM, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struTime', NET_DVR_TIME_EX),
    ('byLampStatus', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPicDataLen', DWORD),
    ('pPicData', String),
    ('byRes', BYTE * 64),
])

NET_DVR_SWITCH_LAMP_ALARM = struct_tagNET_DVR_SWITCH_LAMP_ALARM
LPNET_DVR_SWITCH_LAMP_ALARM = POINTER(struct_tagNET_DVR_SWITCH_LAMP_ALARM)
tagNET_DVR_SWITCH_LAMP_ALARM = struct_tagNET_DVR_SWITCH_LAMP_ALARM
