from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_IOOUT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_IOOUT_PARAM, [
    ('dwSize', DWORD),
    ('byDefaultStatus', BYTE),
    ('byIOOutStatus', BYTE),
    ('byMode', BYTE),
    ('byIOWorkMode', BYTE),
    ('dwTimeDelay', DWORD),
    ('wAheadTime', WORD),
    ('byFreqMulti', BYTE),
    ('byDutyRate', BYTE),
    ('byDetectBrightness', BYTE),
    ('byBrightnessThreld', BYTE),
    ('byFlashLightEnable', BYTE),
    ('byStartHour', BYTE),
    ('byStartMinute', BYTE),
    ('byEndHour', BYTE),
    ('byEndMinute', BYTE),
    ('byAutoPlateBrightness', BYTE),
    ('byIncrBrightEnable', BYTE),
    ('byIncrBrightPercent', BYTE),
    ('wIncrBrightTime', WORD),
    ('byBrightness', BYTE),
    ('byEnvironBright', BYTE),
    ('wDelayCaptureTime', WORD),
])

NET_ITC_IOOUT_PARAM = struct_tagNET_ITC_IOOUT_PARAM
LPNET_ITC_IOOUT_PARAM = POINTER(struct_tagNET_ITC_IOOUT_PARAM)
tagNET_ITC_IOOUT_PARAM = struct_tagNET_ITC_IOOUT_PARAM
