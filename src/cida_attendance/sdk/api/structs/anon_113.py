from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_113(Structure):
    pass

_S(struct_anon_113, [
    ('Output', BYTE * int((32 + 64))),
])

NET_DVR_ALARMOUTSTATUS_V30 = struct_anon_113
LPNET_DVR_ALARMOUTSTATUS_V30 = POINTER(struct_anon_113)
