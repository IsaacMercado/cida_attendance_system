from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_306 import NET_DVR_INQUEST_CDRW
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_anon_307(Structure):
    pass

_S(struct_anon_307, [
    ('dwType', DWORD),
    ('strCDRWNum', NET_DVR_INQUEST_CDRW * 4),
    ('struInquestStartTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 16),
])

NET_DVR_INQUEST_CDRW_STATUS = struct_anon_307
LPNET_DVR_INQUEST_CDRW_STATUS = POINTER(struct_anon_307)
