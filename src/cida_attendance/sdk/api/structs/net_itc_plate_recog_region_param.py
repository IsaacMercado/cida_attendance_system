from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_336 import union_anon_336


class struct_tagNET_ITC_PLATE_RECOG_REGION_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_PLATE_RECOG_REGION_PARAM, [
    ('byMode', BYTE),
    ('byRes1', BYTE * 3),
    ('uRegion', union_anon_336),
    ('byRes', BYTE * 16),
])

NET_ITC_PLATE_RECOG_REGION_PARAM = struct_tagNET_ITC_PLATE_RECOG_REGION_PARAM
LPNET_ITC_PLATE_RECOG_REGION_PARAM = POINTER(struct_tagNET_ITC_PLATE_RECOG_REGION_PARAM)
tagNET_ITC_PLATE_RECOG_REGION_PARAM = struct_tagNET_ITC_PLATE_RECOG_REGION_PARAM
