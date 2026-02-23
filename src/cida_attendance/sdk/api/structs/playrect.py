from ctypes import Structure, c_int

from ..base_classes import _S


class struct___PLAYRECT(Structure):
    pass

_S(struct___PLAYRECT, [
    ('x', c_int),
    ('y', c_int),
    ('uWidth', c_int),
    ('uHeight', c_int),
])

PLAYRECT = struct___PLAYRECT
__PLAYRECT = struct___PLAYRECT
