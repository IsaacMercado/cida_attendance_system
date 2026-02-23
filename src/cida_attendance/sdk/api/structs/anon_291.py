from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_291(Structure):
    pass

_S(struct_anon_291, [
    ('byVGANums', BYTE),
    ('byBNCNums', BYTE),
    ('byHDMINums', BYTE),
    ('byDVINums', BYTE),
    ('byRes', BYTE * 196),
])

