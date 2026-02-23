from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarminfo_fixed_header import NET_DVR_ALRAM_FIXED_HEADER


class struct_NET_DVR_ALARMINFO_V40(Structure):
    pass

_S(struct_NET_DVR_ALARMINFO_V40, [
    ('struAlarmFixedHeader', NET_DVR_ALRAM_FIXED_HEADER),
    ('pAlarmData', POINTER(DWORD)),
])

NET_DVR_ALARMINFO_V40 = struct_NET_DVR_ALARMINFO_V40
LPNET_DVR_ALARMINFO_V40 = POINTER(struct_NET_DVR_ALARMINFO_V40)
NET_DVR_ALARMINFO_V40 = struct_NET_DVR_ALARMINFO_V40
