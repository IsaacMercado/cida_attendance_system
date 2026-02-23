from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_park_external_subinfo import NET_DVR_PARK_EXTERNAL_SUBINFO


class struct_tagNET_DVR_PARKINFO(Structure):
    pass

_S(struct_tagNET_DVR_PARKINFO, [
    ('struNormalParkIOState', NET_DVR_PARK_EXTERNAL_SUBINFO),
    ('struNormalNoParkIOState', NET_DVR_PARK_EXTERNAL_SUBINFO),
    ('struSpecialParkIOState', NET_DVR_PARK_EXTERNAL_SUBINFO),
    ('struSpecialNoParkIOState', NET_DVR_PARK_EXTERNAL_SUBINFO),
    ('byRes', BYTE * 32),
])

NET_DVR_PARKINFO = struct_tagNET_DVR_PARKINFO
LPNET_DVR_PARKINFO = POINTER(struct_tagNET_DVR_PARKINFO)
tagNET_DVR_PARKINFO = struct_tagNET_DVR_PARKINFO
