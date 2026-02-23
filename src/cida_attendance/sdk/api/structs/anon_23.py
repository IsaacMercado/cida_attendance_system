from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_anon_23(Structure):
    pass

_S(struct_anon_23, [
    ('byEnableHandleVILost', BYTE),
    ('strVILostHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
])

NET_DVR_VILOST_V30 = struct_anon_23
LPNET_DVR_VILOST_V30 = POINTER(struct_anon_23)
