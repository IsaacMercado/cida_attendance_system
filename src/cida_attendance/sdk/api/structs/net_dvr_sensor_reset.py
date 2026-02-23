from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_RESET(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_RESET, [
    ('dwSize', DWORD),
    ('bySensorNo', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_SENSOR_RESET = struct_tagNET_DVR_SENSOR_RESET
LPNET_DVR_SENSOR_RESET = POINTER(struct_tagNET_DVR_SENSOR_RESET)
tagNET_DVR_SENSOR_RESET = struct_tagNET_DVR_SENSOR_RESET
