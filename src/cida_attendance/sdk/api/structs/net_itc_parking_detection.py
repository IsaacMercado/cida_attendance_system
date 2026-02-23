from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct__NET_ITC_PARKING_DETECTION_(Structure):
    pass

_S(struct__NET_ITC_PARKING_DETECTION_, [
    ('byEnable', BYTE),
    ('byRes', BYTE),
    ('wDuration', WORD),
    ('wAlarmIntervalTime', WORD),
    ('byRes1', BYTE * 58),
])

NET_ITC_PARKING_DETECTION = struct__NET_ITC_PARKING_DETECTION_
LPNET_ITC_PARKING_DETECTION = POINTER(struct__NET_ITC_PARKING_DETECTION_)
_NET_ITC_PARKING_DETECTION_ = struct__NET_ITC_PARKING_DETECTION_
