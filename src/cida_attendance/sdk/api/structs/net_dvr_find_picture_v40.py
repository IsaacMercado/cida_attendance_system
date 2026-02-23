from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_pic_extra_info_union import NET_DVR_PIC_EXTRA_INFO_UNION


class struct_tagNET_DVR_FIND_PICTURE_V40(Structure):
    pass

_S(struct_tagNET_DVR_FIND_PICTURE_V40, [
    ('sFileName', c_char * 64),
    ('struTime', NET_DVR_TIME),
    ('dwFileSize', DWORD),
    ('sCardNum', c_char * 40),
    ('byPlateColor', BYTE),
    ('byVehicleLogo', BYTE),
    ('byFileType', BYTE),
    ('byRecogResult', BYTE),
    ('sLicense', c_char * 16),
    ('byEventSearchStatus', BYTE),
    ('byRes1', BYTE * 2),
    ('byThermometryUnit', BYTE),
    ('fFaceSnapTemperature', c_float),
    ('byRes', BYTE * 68),
    ('uPicExtraInfo', NET_DVR_PIC_EXTRA_INFO_UNION),
])

NET_DVR_FIND_PICTURE_V40 = struct_tagNET_DVR_FIND_PICTURE_V40
LPNET_DVR_FIND_PICTURE_V40 = POINTER(struct_tagNET_DVR_FIND_PICTURE_V40)
tagNET_DVR_FIND_PICTURE_V40 = struct_tagNET_DVR_FIND_PICTURE_V40
