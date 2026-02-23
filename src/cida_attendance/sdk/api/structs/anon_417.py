from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_417(Structure):
    pass

_S(struct_anon_417, [
    ('dwPosAddr', DWORD),
    ('byRes', BYTE * 948),
])

NET_DVR_POS_AVE = struct_anon_417
LPNET_DVR_AVE = POINTER(struct_anon_417)
