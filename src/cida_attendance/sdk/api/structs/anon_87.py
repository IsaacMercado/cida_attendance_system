from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_87(Structure):
    pass

_S(struct_anon_87, [
    ('dwHDGroupNo', DWORD),
    ('byHDGroupChans', BYTE * int((32 + 32))),
    ('byRes', BYTE * 8),
])

NET_DVR_SINGLE_HDGROUP = struct_anon_87
LPNET_DVR_SINGLE_HDGROUP = POINTER(struct_anon_87)
