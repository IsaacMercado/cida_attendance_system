from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ALARM_RECORD_EXCEPTION(Structure):
    pass

_S(struct_tagNET_ALARM_RECORD_EXCEPTION, [
    ('byReason', BYTE),
    ('byRes1', BYTE * 3),
    ('sVolumeName', BYTE * 32),
    ('dwVolumeID', DWORD),
    ('byRes', BYTE * 452),
])

NET_ALARM_RECORD_EXCEPTION = struct_tagNET_ALARM_RECORD_EXCEPTION
LPNET_ALARM_RECORD_EXCEPTION = POINTER(struct_tagNET_ALARM_RECORD_EXCEPTION)
tagNET_ALARM_RECORD_EXCEPTION = struct_tagNET_ALARM_RECORD_EXCEPTION
