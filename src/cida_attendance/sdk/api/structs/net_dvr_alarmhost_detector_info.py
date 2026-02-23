from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_DETECTOR_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_DETECTOR_INFO, [
    ('dwSize', DWORD),
    ('byDetectorSerialNo', BYTE * 16),
    ('dwAlarmIn', DWORD),
    ('wDetectorType', WORD),
    ('byRes', BYTE * 126),
])

NET_DVR_ALARMHOST_DETECTOR_INFO = struct_tagNET_DVR_ALARMHOST_DETECTOR_INFO
LPNET_DVR_ALARMHOST_DETECTOR_INFO = POINTER(struct_tagNET_DVR_ALARMHOST_DETECTOR_INFO)
tagNET_DVR_ALARMHOST_DETECTOR_INFO = struct_tagNET_DVR_ALARMHOST_DETECTOR_INFO
