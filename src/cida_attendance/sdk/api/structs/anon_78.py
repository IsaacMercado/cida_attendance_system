from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_78(Structure):
    pass

_S(struct_anon_78, [
    ('byIPID', BYTE),
    ('byAlarmOut', BYTE),
    ('byRes', BYTE * 18),
])

NET_DVR_IPALARMOUTINFO = struct_anon_78
LPNET_DVR_IPALARMOUTINFO = POINTER(struct_anon_78)
