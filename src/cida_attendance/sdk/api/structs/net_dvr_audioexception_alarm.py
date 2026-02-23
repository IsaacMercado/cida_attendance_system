from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_AUDIOEXCEPTION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_AUDIOEXCEPTION_ALARM, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byRes1', BYTE),
    ('wAudioDecibel', WORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byRes', BYTE * 62),
])

NET_DVR_AUDIOEXCEPTION_ALARM = struct_tagNET_DVR_AUDIOEXCEPTION_ALARM
LPNET_DVR_AUDIOEXCEPTION_ALARM = POINTER(struct_tagNET_DVR_AUDIOEXCEPTION_ALARM)
tagNET_DVR_AUDIOEXCEPTION_ALARM = struct_tagNET_DVR_AUDIOEXCEPTION_ALARM
