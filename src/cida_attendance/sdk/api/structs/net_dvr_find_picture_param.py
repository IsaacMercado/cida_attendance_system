from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_FIND_PICTURE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_FIND_PICTURE_PARAM, [
    ('dwSize', DWORD),
    ('lChannel', LONG),
    ('byFileType', BYTE),
    ('byNeedCard', BYTE),
    ('byProvince', BYTE),
    ('byEventType', BYTE),
    ('sCardNum', BYTE * 40),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('dwTrafficType', DWORD),
    ('dwVehicleType', DWORD),
    ('dwIllegalType', DWORD),
    ('byLaneNo', BYTE),
    ('bySubHvtType', BYTE),
    ('bySubDriveType', BYTE),
    ('byRes2', BYTE),
    ('sLicense', c_char * 16),
    ('byRegion', BYTE),
    ('byCountry', BYTE),
    ('byArea', BYTE),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
])

NET_DVR_FIND_PICTURE_PARAM = struct_tagNET_DVR_FIND_PICTURE_PARAM
LPNET_DVR_FIND_PICTURE_PARAM = POINTER(struct_tagNET_DVR_FIND_PICTURE_PARAM)
tagNET_DVR_FIND_PICTURE_PARAM = struct_tagNET_DVR_FIND_PICTURE_PARAM
