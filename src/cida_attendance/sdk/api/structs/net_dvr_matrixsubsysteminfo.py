from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIXSUBSYSTEMINFO(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXSUBSYSTEMINFO, [
    ('byMatrixNum', BYTE),
    ('bySubSystemNum', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_MATRIXSUBSYSTEMINFO = struct_tagNET_DVR_MATRIXSUBSYSTEMINFO
LPNET_DVR_MATRIXSUBSYSTEMINFO = POINTER(struct_tagNET_DVR_MATRIXSUBSYSTEMINFO)
tagNET_DVR_MATRIXSUBSYSTEMINFO = struct_tagNET_DVR_MATRIXSUBSYSTEMINFO
