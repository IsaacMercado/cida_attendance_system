from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IP_ALARM_GROUP_NUM(Structure):
    pass

_S(struct_tagNET_DVR_IP_ALARM_GROUP_NUM, [
    ('dwSize', DWORD),
    ('dwIPAlarmInGroup', DWORD),
    ('dwIPAlarmInNum', DWORD),
    ('dwIPAlarmOutGroup', DWORD),
    ('dwIPAlarmOutNum', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_IP_ALARM_GROUP_NUM = struct_tagNET_DVR_IP_ALARM_GROUP_NUM
LPNET_DVR_IP_ALARM_GROUP_NUM = POINTER(struct_tagNET_DVR_IP_ALARM_GROUP_NUM)
tagNET_DVR_IP_ALARM_GROUP_NUM = struct_tagNET_DVR_IP_ALARM_GROUP_NUM
