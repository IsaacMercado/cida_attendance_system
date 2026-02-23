from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_NET_DVR_FD_DATA_COND(Structure):
    pass

_S(struct_NET_DVR_FD_DATA_COND, [
    ('dwSize', DWORD),
    ('szFDID', c_char * 256),
    ('szCheckCode', c_char * 128),
    ('byCover', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_FD_DATA_COND = struct_NET_DVR_FD_DATA_COND
LPNET_DVR_FD_DATA_COND = POINTER(struct_NET_DVR_FD_DATA_COND)
NET_DVR_FD_DATA_COND = struct_NET_DVR_FD_DATA_COND
