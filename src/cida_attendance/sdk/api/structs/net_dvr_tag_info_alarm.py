from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct__NET_DVR_TAG_INFO_ALARM_(Structure):
    pass

_S(struct__NET_DVR_TAG_INFO_ALARM_, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('iRssi', c_int),
    ('byIndexCode', BYTE * 64),
    ('struAcquisitionTime', NET_DVR_TIME_V30),
    ('byRFIDInfo', BYTE * 32),
    ('byRFIDInfoLen', BYTE),
    ('byVoltageLow', BYTE),
    ('byAlarmFlag', BYTE),
    ('byRes', BYTE * 49),
])

NET_DVR_TAG_INFO_ALARM = struct__NET_DVR_TAG_INFO_ALARM_
LPNET_DVR_TAG_INFO_ALARM = POINTER(struct__NET_DVR_TAG_INFO_ALARM_)
_NET_DVR_TAG_INFO_ALARM_ = struct__NET_DVR_TAG_INFO_ALARM_
