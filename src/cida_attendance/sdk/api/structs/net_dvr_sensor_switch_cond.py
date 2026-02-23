from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_SWITCH_COND(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_SWITCH_COND, [
    ('dwSize', DWORD),
    ('byDeviceType', BYTE),
    ('byDeviceID', BYTE),
    ('bySwitch', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_SENSOR_SWITCH_COND = struct_tagNET_DVR_SENSOR_SWITCH_COND
LPNET_DVR_SENSOR_SWITCH_COND = POINTER(struct_tagNET_DVR_SENSOR_SWITCH_COND)
tagNET_DVR_SENSOR_SWITCH_COND = struct_tagNET_DVR_SENSOR_SWITCH_COND
