from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40


class struct_tagNET_DVR_DETECT_FACE(Structure):
    pass

_S(struct_tagNET_DVR_DETECT_FACE, [
    ('dwSize', DWORD),
    ('byEnableDetectFace', BYTE),
    ('byDetectSensitive', BYTE),
    ('byEnableDisplay', BYTE),
    ('byRes', BYTE),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V40),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('dwMaxRelRecordChanNum', DWORD),
    ('dwRelRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * int((32 + 32))),
    ('struHolidayTime', NET_DVR_SCHEDTIME * 8),
    ('wDuration', WORD),
    ('byRes1', BYTE * 30),
])

NET_DVR_DETECT_FACE = struct_tagNET_DVR_DETECT_FACE
LPNET_DVR_DETECT_FACE = POINTER(struct_tagNET_DVR_DETECT_FACE)
tagNET_DVR_DETECT_FACE = struct_tagNET_DVR_DETECT_FACE
