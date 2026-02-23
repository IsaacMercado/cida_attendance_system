from ctypes import Structure, c_int

from ..base_classes import _S


class struct_tagInitInfo(Structure):
    pass

_S(struct_tagInitInfo, [
    ('uWidth', c_int),
    ('uHeight', c_int),
])

INITINFO = struct_tagInitInfo
tagInitInfo = struct_tagInitInfo
