from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_SNAPMODE_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_SNAPMODE_PARAM, [
    ('byVehicleCapMode', BYTE),
    ('byNoVehicleCapMode', BYTE),
    ('byPasserCapMode', BYTE),
    ('byRes', BYTE * 29),
])

NET_ITC_SNAPMODE_PARAM = struct_tagNET_ITC_SNAPMODE_PARAM
LPNET_ITC_SNAPMODE_PARAM = POINTER(struct_tagNET_ITC_SNAPMODE_PARAM)
tagNET_ITC_SNAPMODE_PARAM = struct_tagNET_ITC_SNAPMODE_PARAM
