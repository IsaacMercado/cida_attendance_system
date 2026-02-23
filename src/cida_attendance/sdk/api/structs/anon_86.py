from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_85 import NET_DVR_SINGLE_HD_V50


class struct_anon_86(Structure):
    pass

_S(struct_anon_86, [
    ('dwSize', DWORD),
    ('dwHDCount', DWORD),
    ('struHDInfoV50', NET_DVR_SINGLE_HD_V50 * 33),
    ('byRes', BYTE * 128),
])

NET_DVR_HDCFG_V50 = struct_anon_86
LPNET_DVR_HDCFG_V50 = POINTER(struct_anon_86)
