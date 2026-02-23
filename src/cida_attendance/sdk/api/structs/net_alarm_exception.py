from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ALARM_EXCEPTION(Structure):
    pass

_S(struct_tagNET_ALARM_EXCEPTION, [
    ('dwAlarmType', DWORD),
    ('byExceptionType', BYTE),
    ('byRes', BYTE * 3),
    ('szErrMsg', c_char * 256),
    ('byRes1', BYTE * 248),
])

NET_ALARM_EXCEPTION = struct_tagNET_ALARM_EXCEPTION
LPNET_ALARM_EXCEPTION = POINTER(struct_tagNET_ALARM_EXCEPTION)
tagNET_ALARM_EXCEPTION = struct_tagNET_ALARM_EXCEPTION
