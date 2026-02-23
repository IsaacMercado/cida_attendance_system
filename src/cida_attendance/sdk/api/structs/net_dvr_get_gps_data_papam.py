from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_354 import union_anon_354


class struct_tagNET_DVR_GET_GPS_DATA_PAPAM(Structure):
    pass

_S(struct_tagNET_DVR_GET_GPS_DATA_PAPAM, [
    ('dwCmdType', DWORD),
    ('GpsDataParam', union_anon_354),
])

NET_DVR_GET_GPS_DATA_PARAM = struct_tagNET_DVR_GET_GPS_DATA_PAPAM
LPNET_DVR_GET_GPS_DATA_PARAM = POINTER(struct_tagNET_DVR_GET_GPS_DATA_PAPAM)
tagNET_DVR_GET_GPS_DATA_PAPAM = struct_tagNET_DVR_GET_GPS_DATA_PAPAM
