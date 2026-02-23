from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIXDECODESYSTEMINFO(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXDECODESYSTEMINFO, [
    ('byMatrixNum', BYTE),
    ('bySubSystemNum', BYTE),
    ('byDispChan', BYTE),
    ('bySubDispChan', BYTE),
    ('byRes', BYTE * 12),
])

NET_DVR_MATRIXDECODESYSTEMINFO = struct_tagNET_DVR_MATRIXDECODESYSTEMINFO
LPNET_DVR_MATRIXDECODESYSTEMINFO = POINTER(struct_tagNET_DVR_MATRIXDECODESYSTEMINFO)
tagNET_DVR_MATRIXDECODESYSTEMINFO = struct_tagNET_DVR_MATRIXDECODESYSTEMINFO
