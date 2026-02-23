from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_80(Structure):
    pass

_S(struct_anon_80, [
    ('byIPID', BYTE),
    ('byAlarmIn', BYTE),
    ('byRes', BYTE * 18),
])

NET_DVR_IPALARMININFO = struct_anon_80
LPNET_DVR_IPALARMININFO = POINTER(struct_anon_80)
