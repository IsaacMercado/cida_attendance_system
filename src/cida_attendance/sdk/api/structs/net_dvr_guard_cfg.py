from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40
from .net_dvr_time_detection import NET_DVR_TIME_DETECTION


class struct_tagNET_DVR_GUARD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_GUARD_CFG, [
    ('dwSize', DWORD),
    ('struAlarmSched', (NET_DVR_TIME_DETECTION * 8) * 7),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('dwMaxRelRecordChanNum', DWORD),
    ('dwRelRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * int((32 + 32))),
    ('struHolidayTime', NET_DVR_TIME_DETECTION * 8),
    ('byDirection', BYTE),
    ('byRes', BYTE * 87),
])

NET_DVR_GUARD_CFG = struct_tagNET_DVR_GUARD_CFG
LPNET_DVR_GUARD_CFG = POINTER(struct_tagNET_DVR_GUARD_CFG)
tagNET_DVR_GUARD_CFG = struct_tagNET_DVR_GUARD_CFG
