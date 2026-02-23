from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BUILTIN_PARKLAMP(Structure):
    pass

_S(struct_tagNET_DVR_BUILTIN_PARKLAMP, [
    ('byEnable', BYTE),
    ('byFlicker', BYTE),
    ('byLampColor', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_BUILTIN_PARKLAMP = struct_tagNET_DVR_BUILTIN_PARKLAMP
LPNET_DVR_BUILTIN_PARKLAMP = POINTER(struct_tagNET_DVR_BUILTIN_PARKLAMP)
tagNET_DVR_BUILTIN_PARKLAMP = struct_tagNET_DVR_BUILTIN_PARKLAMP
