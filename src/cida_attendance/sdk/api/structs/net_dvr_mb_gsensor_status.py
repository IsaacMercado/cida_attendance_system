from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MB_GSENSOR_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_MB_GSENSOR_STATUS, [
    ('byGsensorModule', BYTE),
    ('byCurAccX', BYTE * 10),
    ('byCurAccY', BYTE * 10),
    ('byCurAccZ', BYTE * 10),
    ('byRefAccX', BYTE * 10),
    ('byRefAccY', BYTE * 10),
    ('byRefAccZ', BYTE * 10),
    ('byres', BYTE * 3),
])

NET_DVR_MB_GSENSOR_STATUS = struct_tagNET_DVR_MB_GSENSOR_STATUS
LPNET_DVR_MB_GSENSOR_STATUS = POINTER(struct_tagNET_DVR_MB_GSENSOR_STATUS)
tagNET_DVR_MB_GSENSOR_STATUS = struct_tagNET_DVR_MB_GSENSOR_STATUS
