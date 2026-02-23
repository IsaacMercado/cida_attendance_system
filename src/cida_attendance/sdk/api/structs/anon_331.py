from ctypes import Structure

from ..base_classes import _S, BYTE
from .net_dvr_rectcfg import NET_DVR_RECTCFG


class struct_anon_331(Structure):
    pass

_S(struct_anon_331, [
    ('byJoinDecoderId', BYTE * 36),
    ('byDecResolution', BYTE * 36),
    ('struPosition', NET_DVR_RECTCFG),
    ('byRes', BYTE * 80),
])

