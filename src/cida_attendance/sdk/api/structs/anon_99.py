from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_94 import NET_DVR_VGAPARA
from .anon_96 import NET_DVR_MATRIXPARA
from .anon_97 import NET_DVR_VOOUT


class struct_anon_99(Structure):
    pass

_S(struct_anon_99, [
    ('dwSize', DWORD),
    ('struVOOut', NET_DVR_VOOUT * 2),
    ('struVGAPara', NET_DVR_VGAPARA * 1),
    ('struMatrixPara', NET_DVR_MATRIXPARA),
])

NET_DVR_VIDEOOUT = struct_anon_99
LPNET_DVR_VIDEOOUT = POINTER(struct_anon_99)
