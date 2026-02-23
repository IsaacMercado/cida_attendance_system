from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIXCODESYSTEMINFO(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXCODESYSTEMINFO, [
    ('byMatrixNum', BYTE),
    ('bySubSystemNum', BYTE),
    ('byChan', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_MATRIXCODESYSTEMINFO = struct_tagNET_DVR_MATRIXCODESYSTEMINFO
LPNET_DVR_MATRIXCODESYSTEMINFO = POINTER(struct_tagNET_DVR_MATRIXCODESYSTEMINFO)
tagNET_DVR_MATRIXCODESYSTEMINFO = struct_tagNET_DVR_MATRIXCODESYSTEMINFO
