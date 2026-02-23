from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct__NET_DVR_NORMAL_SCHEDTIME_(Structure):
    pass

_S(struct__NET_DVR_NORMAL_SCHEDTIME_, [
    ('struTime', NET_DVR_SCHEDTIME),
    ('byAlarmType', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_NORMAL_SCHEDTIME = struct__NET_DVR_NORMAL_SCHEDTIME_
LPNET_DVR_NORMAL_SCHEDTIME = POINTER(struct__NET_DVR_NORMAL_SCHEDTIME_)
_NET_DVR_NORMAL_SCHEDTIME_ = struct__NET_DVR_NORMAL_SCHEDTIME_
