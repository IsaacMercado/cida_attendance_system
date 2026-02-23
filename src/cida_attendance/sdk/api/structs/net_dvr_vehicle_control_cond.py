from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLE_CONTROL_COND(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_CONTROL_COND, [
    ('dwChannel', DWORD),
    ('dwOperateType', DWORD),
    ('sLicense', c_char * 16),
    ('sCardNo', c_char * 48),
    ('byListType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwDataIndex', DWORD),
    ('byRes', BYTE * 116),
])

NET_DVR_VEHICLE_CONTROL_COND = struct_tagNET_DVR_VEHICLE_CONTROL_COND
LPNET_DVR_VEHICLE_CONTROL_COND = POINTER(struct_tagNET_DVR_VEHICLE_CONTROL_COND)
tagNET_DVR_VEHICLE_CONTROL_COND = struct_tagNET_DVR_VEHICLE_CONTROL_COND
