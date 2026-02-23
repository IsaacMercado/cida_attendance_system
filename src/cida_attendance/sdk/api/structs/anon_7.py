from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_7(Structure):
    pass

_S(struct_anon_7, [
    ('dwHandleType', DWORD),
    ('byRelAlarmOut', BYTE * int((32 + 64))),
])

NET_DVR_HANDLEEXCEPTION_V30 = struct_anon_7
LPNET_DVR_HANDLEEXCEPTION_V30 = POINTER(struct_anon_7)
