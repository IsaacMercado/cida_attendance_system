from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_19 import NET_DVR_MOTION
from .anon_22 import NET_DVR_HIDEALARM
from .anon_24 import NET_DVR_VILOST


class struct_anon_30(Structure):
    pass

_S(struct_anon_30, [
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
    ('wHideAreaTopLeftX', WORD),
    ('wHideAreaTopLeftY', WORD),
    ('wHideAreaWidth', WORD),
    ('wHideAreaHeight', WORD),
    ('dwShowOsd', DWORD),
    ('wOSDTopLeftX', WORD),
    ('wOSDTopLeftY', WORD),
    ('byOSDType', BYTE),
    ('byDispWeek', BYTE),
    ('byOSDAttrib', BYTE),
    ('reservedData2', c_char),
])

NET_DVR_PICCFG = struct_anon_30
LPNET_DVR_PICCFG = POINTER(struct_anon_30)
