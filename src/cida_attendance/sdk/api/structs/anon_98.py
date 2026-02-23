from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_94 import NET_DVR_VGAPARA
from .anon_95 import NET_DVR_MATRIXPARA_V30
from .anon_97 import NET_DVR_VOOUT


class struct_anon_98(Structure):
    pass

_S(struct_anon_98, [
    ('dwSize', DWORD),
    ('struVOOut', NET_DVR_VOOUT * 4),
    ('struVGAPara', NET_DVR_VGAPARA * 4),
    ('struMatrixPara', NET_DVR_MATRIXPARA_V30 * 16),
    ('byRes', BYTE * 16),
])

NET_DVR_VIDEOOUT_V30 = struct_anon_98
LPNET_DVR_VIDEOOUT_V30 = POINTER(struct_anon_98)
