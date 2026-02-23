from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__tagNET_ITS_HANDOVER_INFO(Structure):
    pass

_S(struct__tagNET_ITS_HANDOVER_INFO, [
    ('dwSize', DWORD),
    ('byOperatorName', BYTE * 32),
    ('byOperatorCard', BYTE * 24),
    ('byStartTime', BYTE * 32),
    ('byEndTime', BYTE * 32),
    ('fTotal_Pay', c_float),
    ('dwTotal_Records', DWORD),
    ('byRes', BYTE * 64),
])

NET_ITS_HANDOVER_INFO = struct__tagNET_ITS_HANDOVER_INFO
LPNET_ITS_HANDOVER_INFO = POINTER(struct__tagNET_ITS_HANDOVER_INFO)
_tagNET_ITS_HANDOVER_INFO = struct__tagNET_ITS_HANDOVER_INFO
