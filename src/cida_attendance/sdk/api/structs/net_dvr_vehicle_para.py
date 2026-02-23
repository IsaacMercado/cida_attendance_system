from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLE_PARA(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_PARA, [
    ('sLicense', BYTE * 16),
    ('byCountry', BYTE),
    ('byRes', BYTE * 239),
])

NET_DVR_VEHICLE_PARA = struct_tagNET_DVR_VEHICLE_PARA
LPNET_DVR_VEHICLE_PARA = POINTER(struct_tagNET_DVR_VEHICLE_PARA)
tagNET_DVR_VEHICLE_PARA = struct_tagNET_DVR_VEHICLE_PARA
