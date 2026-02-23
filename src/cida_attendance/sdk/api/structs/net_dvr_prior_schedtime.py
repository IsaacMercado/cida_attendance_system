from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_normal_schedtime import NET_DVR_NORMAL_SCHEDTIME
from .net_dvr_scheddate import NET_DVR_SCHEDDATE


class struct__NET_DVR_PRIOR_SCHEDTIME_(Structure):
    pass

_S(struct__NET_DVR_PRIOR_SCHEDTIME_, [
    ('dwSize', DWORD),
    ('struData', NET_DVR_SCHEDDATE),
    ('struOneDayTime', NET_DVR_NORMAL_SCHEDTIME * 8),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('bySubSystem', BYTE * 32),
    ('byMandatoryAlarm', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_PRIOR_SCHEDTIME = struct__NET_DVR_PRIOR_SCHEDTIME_
LPNET_DVR_PRIOR_SCHEDTIME = POINTER(struct__NET_DVR_PRIOR_SCHEDTIME_)
_NET_DVR_PRIOR_SCHEDTIME_ = struct__NET_DVR_PRIOR_SCHEDTIME_
