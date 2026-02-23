from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_148 import NET_DVR_NTPPARA


class struct_anon_374(Structure):
    pass

_S(struct_anon_374, [
    ('struNtpPara', NET_DVR_NTPPARA),
    ('byRes1', BYTE * 660),
])

