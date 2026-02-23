from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_304(Structure):
    pass

_S(struct_anon_304, [
    ('sFileName', c_char * 36),
    ('dwFileLen', DWORD),
])

NET_DVR_INQUEST_FILEINFO = struct_anon_304
LPNET_DVR_INQUEST_FILEINFO = POINTER(struct_anon_304)
