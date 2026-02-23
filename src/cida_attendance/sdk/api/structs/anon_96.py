from ctypes import Structure

from ..base_classes import _S, WORD


class struct_anon_96(Structure):
    pass

_S(struct_anon_96, [
    ('wDisplayLogo', WORD),
    ('wDisplayOsd', WORD),
])

NET_DVR_MATRIXPARA = struct_anon_96
