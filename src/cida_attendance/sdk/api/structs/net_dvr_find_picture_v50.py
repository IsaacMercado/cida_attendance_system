from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_address import NET_DVR_ADDRESS
from .net_dvr_pic_extra_info_union import NET_DVR_PIC_EXTRA_INFO_UNION


class struct_tagNET_DVR_FIND_PICTURE_V50(Structure):
    pass

_S(struct_tagNET_DVR_FIND_PICTURE_V50, [
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
    ('struAddr', NET_DVR_ADDRESS),
    ('byISO8601', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 253),
    ('uPicExtraInfo', NET_DVR_PIC_EXTRA_INFO_UNION),
])

NET_DVR_FIND_PICTURE_V50 = struct_tagNET_DVR_FIND_PICTURE_V50
LPNET_DVR_FIND_PICTURE_V50 = POINTER(struct_tagNET_DVR_FIND_PICTURE_V50)
tagNET_DVR_FIND_PICTURE_V50 = struct_tagNET_DVR_FIND_PICTURE_V50
