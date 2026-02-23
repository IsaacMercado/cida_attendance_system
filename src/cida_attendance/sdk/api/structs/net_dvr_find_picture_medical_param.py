from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_FIND_PICTURE_MEDICAL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_FIND_PICTURE_MEDICAL_PARAM, [
    ('dwSize', DWORD),
    ('lChannel', LONG),
    ('byFileType', BYTE),
    ('byNeedCard', BYTE),
    ('byProvince', BYTE),
    ('byRes1', BYTE),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('szPatientID', c_char * 64),
    ('byRes', BYTE * 256),
])

NET_DVR_FIND_PICTURE_MEDICAL_PARAM = struct_tagNET_DVR_FIND_PICTURE_MEDICAL_PARAM
LPNET_DVR_FIND_PICTURE_MEDICAL_PARAM = POINTER(struct_tagNET_DVR_FIND_PICTURE_MEDICAL_PARAM)
tagNET_DVR_FIND_PICTURE_MEDICAL_PARAM = struct_tagNET_DVR_FIND_PICTURE_MEDICAL_PARAM
