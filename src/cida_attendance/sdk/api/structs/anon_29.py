from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_19 import NET_DVR_MOTION
from .anon_22 import NET_DVR_HIDEALARM
from .anon_24 import NET_DVR_VILOST
from .anon_25 import NET_DVR_SHELTER


class struct_anon_29(Structure):
    pass

_S(struct_anon_29, [
    ('dwSize', DWORD),
    ('sChanName', BYTE * 32),
    ('dwVideoFormat', DWORD),
    ('byBrightness', BYTE),
    ('byContrast', BYTE),
    ('bySaturation', BYTE),
    ('byHue', BYTE),
    ('dwShowChanName', DWORD),
    ('wShowNameTopLeftX', WORD),
    ('wShowNameTopLeftY', WORD),
    ('struVILost', NET_DVR_VILOST),
    ('struMotion', NET_DVR_MOTION),
    ('struHideAlarm', NET_DVR_HIDEALARM),
    ('dwEnableHide', DWORD),
    ('struShelter', NET_DVR_SHELTER * 4),
    ('dwShowOsd', DWORD),
    ('wOSDTopLeftX', WORD),
    ('wOSDTopLeftY', WORD),
    ('byOSDType', BYTE),
    ('byDispWeek', BYTE),
    ('byOSDAttrib', BYTE),
    ('byHourOsdType', BYTE),
])

NET_DVR_PICCFG_EX = struct_anon_29
LPNET_DVR_PICCFG_EX = POINTER(struct_anon_29)
