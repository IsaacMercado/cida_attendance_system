from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_capture_day import NET_DVR_CAPTURE_DAY
from .net_dvr_capture_sched import NET_DVR_CAPTURE_SCHED


class struct_tagNET_DVR_SCHED_CAPTURECFG(Structure):
    pass

_S(struct_tagNET_DVR_SCHED_CAPTURECFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struCaptureDay', NET_DVR_CAPTURE_DAY * 7),
    ('struCaptureSched', (NET_DVR_CAPTURE_SCHED * 8) * 7),
    ('struCaptureHoliday', NET_DVR_CAPTURE_DAY),
    ('struHolidaySched', NET_DVR_CAPTURE_SCHED * 8),
    ('dwRecorderDuration', DWORD),
    ('dwDelayTime', DWORD),
    ('byRes', BYTE * 36),
])

NET_DVR_SCHED_CAPTURECFG = struct_tagNET_DVR_SCHED_CAPTURECFG
LPNET_DVR_SCHED_CAPTURECFG = POINTER(struct_tagNET_DVR_SCHED_CAPTURECFG)
tagNET_DVR_SCHED_CAPTURECFG = struct_tagNET_DVR_SCHED_CAPTURECFG
