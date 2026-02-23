from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_event_info_list import NET_DVR_EVENT_INFO_LIST
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_RULE_INFO_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_RULE_INFO_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struEventInfoList', NET_DVR_EVENT_INFO_LIST),
    ('byRes2', BYTE * 40),
])

NET_DVR_RULE_INFO_ALARM = struct_tagNET_DVR_RULE_INFO_ALARM
LPNET_DVR_RULE_INFO_ALARM = POINTER(struct_tagNET_DVR_RULE_INFO_ALARM)
tagNET_DVR_RULE_INFO_ALARM = struct_tagNET_DVR_RULE_INFO_ALARM
