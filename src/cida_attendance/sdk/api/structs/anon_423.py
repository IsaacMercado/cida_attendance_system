from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_423(Structure):
    pass

_S(struct_anon_423, [
    ('dwSize', DWORD),
    ('dwDataIndex', DWORD),
    ('sOperateIndex', c_char * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_VEHICLE_CONTROL_LIST_DSALARM = struct_anon_423
LPNET_DVR_VEHICLE_CONTROL_LIST_DSALARM = POINTER(struct_anon_423)
