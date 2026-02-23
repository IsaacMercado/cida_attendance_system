from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_116(Structure):
    pass

_S(struct_anon_116, [
    ('code', BYTE * 12),
])

NET_DVR_FRAMETYPECODE = struct_anon_116
