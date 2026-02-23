from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BASE_STATION_INFO_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_BASE_STATION_INFO_ALARM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('sNetBarWaCode', c_char * 16),
    ('sCollectionEquipmentID', c_char * 24),
    ('sMCC', c_char * 4),
    ('sMNC', c_char * 4),
    ('sLAC', c_char * 36),
    ('sCI', c_char * 36),
    ('sBSCI', c_char * 36),
    ('sBCCH', c_char * 36),
    ('sLEV', c_char * 36),
    ('sCollectionEquipmentLongitude', c_char * 12),
    ('sCollectionEquipmentLatitude', c_char * 12),
    ('sCaptureTime', c_char * 20),
    ('byRes', BYTE * 256),
])

NET_DVR_BASE_STATION_INFO_ALARM = struct_tagNET_DVR_BASE_STATION_INFO_ALARM
LPNET_DVR_BASE_STATION_INFO_ALARM = POINTER(struct_tagNET_DVR_BASE_STATION_INFO_ALARM)
tagNET_DVR_BASE_STATION_INFO_ALARM = struct_tagNET_DVR_BASE_STATION_INFO_ALARM
