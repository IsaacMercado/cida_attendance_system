from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_429(Structure):
    pass

_S(struct_anon_429, [
    ('byDefaultState', BYTE),
    ('byWorkState', BYTE),
    ('byFreqMulti', BYTE),
    ('byDutyRatio', BYTE),
    ('byRes', BYTE * 3),
    ('byFlashLightEnable', BYTE),
    ('struFlashLightTime', NET_DVR_SCHEDTIME),
    ('byRes1', BYTE * 116),
])

