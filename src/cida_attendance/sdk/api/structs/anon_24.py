from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_8 import NET_DVR_HANDLEEXCEPTION


class struct_anon_24(Structure):
    pass

_S(struct_anon_24, [
    ('byEnableHandleVILost', BYTE),
    ('strVILostHandleType', NET_DVR_HANDLEEXCEPTION),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 4) * 7),
])

NET_DVR_VILOST = struct_anon_24
LPNET_DVR_VILOST = POINTER(struct_anon_24)
