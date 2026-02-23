from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_87 import NET_DVR_SINGLE_HDGROUP


class struct_anon_88(Structure):
    pass

_S(struct_anon_88, [
    ('dwSize', DWORD),
    ('dwHDGroupCount', DWORD),
    ('struHDGroupAttr', NET_DVR_SINGLE_HDGROUP * 16),
])

NET_DVR_HDGROUP_CFG = struct_anon_88
LPNET_DVR_HDGROUP_CFG = POINTER(struct_anon_88)
