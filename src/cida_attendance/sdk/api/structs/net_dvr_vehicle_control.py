from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLE_CONTROL(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_CONTROL, [
    ('byGateOperateType', BYTE),
    ('byRes1', BYTE),
    ('wAlarmOperateType', WORD),
    ('byRes2', BYTE * 8),
])

NET_DVR_VEHICLE_CONTROL = struct_tagNET_DVR_VEHICLE_CONTROL
LPNET_DVR_VEHICLE_CONTROL = POINTER(struct_tagNET_DVR_VEHICLE_CONTROL)
tagNET_DVR_VEHICLE_CONTROL = struct_tagNET_DVR_VEHICLE_CONTROL
