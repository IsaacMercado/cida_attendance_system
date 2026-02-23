from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_386 import NET_DVR_SCHEDULE_DAYTIME
from .anon_388 import NET_DVR_MOTION_MULTI_AREAPARAM


class struct_anon_389(Structure):
    pass

_S(struct_anon_389, [
    ('byDayNightCtrl', BYTE),
    ('byAllMotionSensitive', BYTE),
    ('byRes', BYTE * 2),
    ('struScheduleTime', NET_DVR_SCHEDULE_DAYTIME),
    ('struMotionMultiAreaParam', NET_DVR_MOTION_MULTI_AREAPARAM * 24),
    ('byRes1', BYTE * 60),
])

NET_DVR_MOTION_MULTI_AREA = struct_anon_389
LPNET_DVR_MOTION_MULTI_AREA = POINTER(struct_anon_389)
