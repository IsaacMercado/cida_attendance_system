from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_PLATE_RECOG_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_PLATE_RECOG_PARAM, [
    ('byDefaultCHN', BYTE * 3),
    ('byEnable', BYTE),
    ('dwRecogMode', DWORD),
    ('byVehicleLogoRecog', BYTE),
    ('byProvince', BYTE),
    ('byRegion', BYTE),
    ('byCountry', BYTE),
    ('wPlatePixelWidthMin', WORD),
    ('wPlatePixelWidthMax', WORD),
    ('byRes', BYTE * 24),
])

NET_ITC_PLATE_RECOG_PARAM = struct_tagNET_ITC_PLATE_RECOG_PARAM
LPNET_ITC_PLATE_RECOG_PARAM = POINTER(struct_tagNET_ITC_PLATE_RECOG_PARAM)
tagNET_ITC_PLATE_RECOG_PARAM = struct_tagNET_ITC_PLATE_RECOG_PARAM
