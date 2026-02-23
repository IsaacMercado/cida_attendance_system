from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_155(Structure):
    pass

_S(struct_anon_155, [
    ('sNfsHostIPAddr', c_char * 16),
    ('sNfsDirectory', BYTE * 128),
])

NET_DVR_SINGLE_NFS = struct_anon_155
LPNET_DVR_SINGLE_NFS = POINTER(struct_anon_155)
