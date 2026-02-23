from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLE_WEIGHT_RESULT_(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_WEIGHT_RESULT_, [
    ('byIsOverWeight', BYTE),
    ('byAxleNum', BYTE),
    ('wAxleModel', WORD),
    ('fOverWeight', c_float),
    ('fWeight', c_float),
    ('fLimitWeight', c_float),
    ('fAxleLen', c_float),
    ('sDevDescInfo', c_char * 64),
    ('wAxleWeight', WORD * 10),
    ('wAxleDistance', WORD * 10),
    ('dwLength', DWORD),
    ('dwWidth', DWORD),
    ('dwHeight', DWORD),
    ('byTollwayVehicleType', BYTE),
    ('byRes2', BYTE * 11),
])

NET_DVR_VEHICLE_WEIGHT_RESULT = struct_tagNET_DVR_VEHICLE_WEIGHT_RESULT_
LPNET_DVR_VEHICLE_WEIGHT_RESULT = POINTER(struct_tagNET_DVR_VEHICLE_WEIGHT_RESULT_)
tagNET_DVR_VEHICLE_WEIGHT_RESULT_ = struct_tagNET_DVR_VEHICLE_WEIGHT_RESULT_
