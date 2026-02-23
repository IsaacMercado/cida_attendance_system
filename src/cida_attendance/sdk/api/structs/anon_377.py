from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_141 import NET_DVR_EMAILCFG_V30


class struct_anon_377(Structure):
    pass

_S(struct_anon_377, [
    ('struEmailPara', NET_DVR_EMAILCFG_V30),
    ('byRes1', BYTE * 80),
])

