from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CONTROL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CONTROL_PARAM, [
    ('dwSize', DWORD),
    ('sDeviceID', BYTE * 32),
    ('wChan', WORD),
    ('byIndex', BYTE),
    ('byRes1', BYTE),
    ('dwControlParam', DWORD),
    ('byMandatoryAlarm', BYTE),
    ('byRes2', BYTE),
    ('wZoneIndex', WORD),
    ('byOperatorCode', BYTE * 16),
    ('dwPlanNo', DWORD),
    ('byRes3', BYTE * 8),
])

NET_DVR_CONTROL_PARAM = struct_tagNET_DVR_CONTROL_PARAM
LPNET_DVR_CONTROL_PARAM = POINTER(struct_tagNET_DVR_CONTROL_PARAM)
tagNET_DVR_CONTROL_PARAM = struct_tagNET_DVR_CONTROL_PARAM
