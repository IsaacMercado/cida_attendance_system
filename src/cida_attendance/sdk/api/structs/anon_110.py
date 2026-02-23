from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_110(Structure):
    pass

_S(struct_anon_110, [
    ('dwVolume', DWORD),
    ('dwFreeSpace', DWORD),
    ('dwHardDiskStatic', DWORD),
])

NET_DVR_DISKSTATE = struct_anon_110
LPNET_DVR_DISKSTATE = POINTER(struct_anon_110)
