from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_ALARM_STREAM_EXCEPTION(Structure):
    pass

_S(struct_tagNET_ALARM_STREAM_EXCEPTION, [
    ('struIP', NET_DVR_IPADDR),
    ('dwChanNo', DWORD),
    ('dwIDIndex', DWORD),
    ('sName', BYTE * 32),
    ('byExceptionCase', BYTE),
    ('byRes', BYTE * 307),
])

NET_ALARM_STREAM_EXCEPTION = struct_tagNET_ALARM_STREAM_EXCEPTION
LPNET_ALARM_STREAM_EXCEPTION = POINTER(struct_tagNET_ALARM_STREAM_EXCEPTION)
tagNET_ALARM_STREAM_EXCEPTION = struct_tagNET_ALARM_STREAM_EXCEPTION
