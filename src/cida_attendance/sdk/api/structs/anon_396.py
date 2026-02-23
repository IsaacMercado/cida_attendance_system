from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_386 import NET_DVR_SCHEDULE_DAYTIME
from .net_dvr_cameraparamcfg_ex import NET_DVR_CAMERAPARAMCFG_EX


class struct_anon_396(Structure):
    pass

_S(struct_anon_396, [
    ('dwSize', DWORD),
    ('byWorkType', BYTE),
    ('byRes', BYTE * 3),
    ('struDayNightScheduleTime', NET_DVR_SCHEDULE_DAYTIME),
    ('struSelfAdaptiveParam', NET_DVR_CAMERAPARAMCFG_EX),
    ('struDayIspAdvanceParam', NET_DVR_CAMERAPARAMCFG_EX),
    ('struNightIspAdvanceParam', NET_DVR_CAMERAPARAMCFG_EX),
    ('byRes1', BYTE * 512),
])

NET_DVR_ISP_CAMERAPARAMCFG = struct_anon_396
LPNET_DVR_ISP_CAMERAPARAMCFG = POINTER(struct_anon_396)
