from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_155 import NET_DVR_SINGLE_NFS


class struct_anon_156(Structure):
    pass

_S(struct_anon_156, [
    ('dwSize', DWORD),
    ('struNfsDiskParam', NET_DVR_SINGLE_NFS * 8),
])

NET_DVR_NFSCFG = struct_anon_156
LPNET_DVR_NFSCFG = POINTER(struct_anon_156)
