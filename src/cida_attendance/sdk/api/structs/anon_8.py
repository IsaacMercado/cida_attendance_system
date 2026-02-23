from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_8(Structure):
    pass

_S(struct_anon_8, [
    ('dwHandleType', DWORD),
    ('byRelAlarmOut', BYTE * 4),
])

NET_DVR_HANDLEEXCEPTION = struct_anon_8
LPNET_DVR_HANDLEEXCEPTION = POINTER(struct_anon_8)
