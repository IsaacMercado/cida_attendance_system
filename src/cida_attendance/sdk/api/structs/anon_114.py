from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_114(Structure):
    pass

_S(struct_anon_114, [
    ('Output', BYTE * 4),
])

NET_DVR_ALARMOUTSTATUS = struct_anon_114
LPNET_DVR_ALARMOUTSTATUS = POINTER(struct_anon_114)
