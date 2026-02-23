from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_294(Structure):
    pass

_S(struct_anon_294, [
    ('dwHandleType', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE),
    ('wDuration', WORD),
    ('byAlarmOutTriggered', BYTE * 32),
    ('byRes1', BYTE * 8),
])

NET_ITC_HANDLEEXCEPTION = struct_anon_294
LPNET_ITC_HANDLEEXCEPTION = POINTER(struct_anon_294)
