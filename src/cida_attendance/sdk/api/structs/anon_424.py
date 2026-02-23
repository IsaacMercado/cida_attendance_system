from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_424(Structure):
    pass

_S(struct_anon_424, [
    ('dwSize', DWORD),
    ('dwDelType', DWORD),
    ('sLicense', c_char * 16),
    ('sCardNo', c_char * 48),
    ('byPlateType', BYTE),
    ('byPlateColor', BYTE),
    ('byOperateType', BYTE),
    ('byListType', BYTE),
    ('dwDataIndex', DWORD),
    ('sOperateIndex', c_char * 32),
    ('byRes', BYTE * 24),
])

NET_DVR_VEHICLE_CONTROL_DELINFO = struct_anon_424
LPNET_DVR_VEHICLE_CONTROL_DELINFO = POINTER(struct_anon_424)
