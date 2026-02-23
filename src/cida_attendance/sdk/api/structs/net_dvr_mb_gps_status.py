from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MB_GPS_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_MB_GPS_STATUS, [
    ('byGPSModule', BYTE),
    ('byPositionStatus', BYTE),
    ('bySignalStrength', BYTE),
    ('byres', BYTE * 5),
])

NET_DVR_MB_GPS_STATUS = struct_tagNET_DVR_MB_GPS_STATUS
LPNET_DVR_MB_GPS_STATUS = POINTER(struct_tagNET_DVR_MB_GPS_STATUS)
tagNET_DVR_MB_GPS_STATUS = struct_tagNET_DVR_MB_GPS_STATUS
