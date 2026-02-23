from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ZONE_ALARM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ZONE_ALARM_INFO, [
    ('byZoneName', BYTE * 32),
    ('dwZonendex', DWORD),
    ('byZoneType', BYTE),
    ('byRes', BYTE * 219),
])

NET_DVR_ZONE_ALARM_INFO = struct_tagNET_DVR_ZONE_ALARM_INFO
LPNET_DVR_ZONE_ALARM_INFO = POINTER(struct_tagNET_DVR_ZONE_ALARM_INFO)
tagNET_DVR_ZONE_ALARM_INFO = struct_tagNET_DVR_ZONE_ALARM_INFO
