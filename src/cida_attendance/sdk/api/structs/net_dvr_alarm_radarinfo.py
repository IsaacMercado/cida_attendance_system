from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_RADARINFO(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_RADARINFO, [
    ('dwSize', DWORD),
    ('dwRadarTriggerTimeSecond', DWORD),
    ('dwRadarTriggerTimeMSecond', DWORD),
    ('dwVedioTriggerTimeSecond', DWORD),
    ('dwVedioTriggerTimeMSecond', DWORD),
    ('dwVedioRadarDiffTimeMSecond', DWORD),
    ('dwRadarSpeed', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_ALARM_RADARINFO = struct_tagNET_DVR_ALARM_RADARINFO
LPNET_DVR_ALARM_RADARINFO = POINTER(struct_tagNET_DVR_ALARM_RADARINFO)
tagNET_DVR_ALARM_RADARINFO = struct_tagNET_DVR_ALARM_RADARINFO
