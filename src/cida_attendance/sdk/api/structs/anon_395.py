from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_20 import NET_DVR_HIDEALARM_V40
from .anon_25 import NET_DVR_SHELTER
from .anon_27 import NET_DVR_RGB_COLOR
from .anon_392 import NET_DVR_MOTION_V40
from .anon_393 import NET_DVR_VILOST_V40
from .anon_394 import NET_DVR_VICOLOR


class struct_anon_395(Structure):
    pass

_S(struct_anon_395, [
    ('dwSize', DWORD),
    ('sChanName', BYTE * 32),
    ('dwVideoFormat', DWORD),
    ('struViColor', NET_DVR_VICOLOR),
    ('dwShowChanName', DWORD),
    ('wShowNameTopLeftX', WORD),
    ('wShowNameTopLeftY', WORD),
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
    ('struVILost', NET_DVR_VILOST_V40),
    ('struAULost', NET_DVR_VILOST_V40),
    ('struMotion', NET_DVR_MOTION_V40),
    ('struHideAlarm', NET_DVR_HIDEALARM_V40),
    ('struOsdColor', NET_DVR_RGB_COLOR),
    ('dwBoundary', DWORD),
    ('struOsdBkColor', NET_DVR_RGB_COLOR),
    ('byOSDBkColorMode', BYTE),
    ('byUpDownBoundary', BYTE),
    ('byLeftRightBoundary', BYTE),
    ('byAngleEnabled', BYTE),
    ('wTiltAngleTopLeftX', WORD),
    ('wTiltAngleTopLeftY', WORD),
    ('byRes', BYTE * 108),
])

NET_DVR_PICCFG_V40 = struct_anon_395
LPNET_DVR_PICCFG_V40 = POINTER(struct_anon_395)
