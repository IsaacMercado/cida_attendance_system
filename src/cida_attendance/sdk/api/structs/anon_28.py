from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_18 import NET_DVR_MOTION_V30
from .anon_21 import NET_DVR_HIDEALARM_V30
from .anon_23 import NET_DVR_VILOST_V30
from .anon_25 import NET_DVR_SHELTER
from .anon_27 import NET_DVR_RGB_COLOR


class struct_anon_28(Structure):
    pass

_S(struct_anon_28, [
    ('dwSize', DWORD),
    ('sChanName', BYTE * 32),
    ('dwVideoFormat', DWORD),
    ('byReservedData', BYTE * 64),
    ('dwShowChanName', DWORD),
    ('wShowNameTopLeftX', WORD),
    ('wShowNameTopLeftY', WORD),
    ('struVILost', NET_DVR_VILOST_V30),
    ('struRes', NET_DVR_VILOST_V30),
    ('struMotion', NET_DVR_MOTION_V30),
    ('struHideAlarm', NET_DVR_HIDEALARM_V30),
    ('dwEnableHide', DWORD),
    ('struShelter', NET_DVR_SHELTER * 4),
    ('dwShowOsd', DWORD),
    ('wOSDTopLeftX', WORD),
    ('wOSDTopLeftY', WORD),
    ('byOSDType', BYTE),
    ('byDispWeek', BYTE),
    ('byOSDAttrib', BYTE),
    ('byHourOSDType', BYTE),
    ('byFontSize', BYTE),
    ('byOSDColorType', BYTE),
    ('byAlignment', BYTE),
    ('byOSDMilliSecondEnable', BYTE),
    ('struOsdColor', NET_DVR_RGB_COLOR),
    ('dwBoundary', DWORD),
    ('struOsdBkColor', NET_DVR_RGB_COLOR),
    ('byOSDBkColorMode', BYTE),
    ('byUpDownBoundary', BYTE),
    ('byLeftRightBoundary', BYTE),
    ('byAngleEnabled', BYTE),
    ('wTiltAngleTopLeftX', WORD),
    ('wTiltAngleTopLeftY', WORD),
    ('byRes', BYTE * 40),
])

NET_DVR_PICCFG_V30 = struct_anon_28
LPNET_DVR_PICCFG_V30 = POINTER(struct_anon_28)
