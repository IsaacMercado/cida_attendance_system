from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HANDLEEXCEPTION_V40(Structure):
    pass

_S(struct_tagNET_DVR_HANDLEEXCEPTION_V40, [
    ('dwHandleType', DWORD),
    ('dwMaxRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOut', DWORD * int((32 + 32))),
    ('byWhiteLightDurationTime', BYTE),
    ('byBrightness', BYTE),
    ('byAudioType', BYTE),
    ('byTimes', BYTE),
    ('byRes', BYTE * 60),
])

NET_DVR_HANDLEEXCEPTION_V40 = struct_tagNET_DVR_HANDLEEXCEPTION_V40
LPNET_DVR_HANDLEEXCEPTION_V40 = POINTER(struct_tagNET_DVR_HANDLEEXCEPTION_V40)
tagNET_DVR_HANDLEEXCEPTION_V40 = struct_tagNET_DVR_HANDLEEXCEPTION_V40
