from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_NET_DVR_PARKING_DATASTATE_INFO(Structure):
    pass

_S(struct_NET_DVR_PARKING_DATASTATE_INFO, [
    ('dwSize', DWORD),
    ('szAppSerialNum', c_char * 32),
    ('dwParkingNum', DWORD),
    ('dwUpdataSerialNum', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_PARKING_DATASTATE_INFO = struct_NET_DVR_PARKING_DATASTATE_INFO
LPNET_DVR_PARKING_DATASTATE_INFO = POINTER(struct_NET_DVR_PARKING_DATASTATE_INFO)
NET_DVR_PARKING_DATASTATE_INFO = struct_NET_DVR_PARKING_DATASTATE_INFO
