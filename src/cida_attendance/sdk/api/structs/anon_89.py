from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_89(Structure):
    pass

_S(struct_anon_89, [
    ('dwSize', DWORD),
    ('dwMajorScale', DWORD),
    ('dwMinorScale', DWORD),
    ('dwRes', DWORD * 2),
])

NET_DVR_SCALECFG = struct_anon_89
LPNET_DVR_SCALECFG = POINTER(struct_anon_89)
