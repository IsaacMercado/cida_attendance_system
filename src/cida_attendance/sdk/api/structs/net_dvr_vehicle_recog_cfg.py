from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_VEHICLE_RECOG_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_RECOG_CFG, [
    ('dwSize', DWORD),
    ('sDataIndex', c_char * 64),
    ('wTaskNo', WORD),
    ('byRes1', BYTE * 2),
    ('struPlateRect', NET_VCA_RECT),
    ('sLicense', c_char * 16),
    ('dwRecogOperate', DWORD),
    ('dwDataUploadType', DWORD),
    ('dwPostID', DWORD),
    ('struPostTime', NET_DVR_TIME_V30),
    ('dwJsonLen', DWORD),
    ('pJsonBuffer', POINTER(BYTE)),
    ('byRes', BYTE * 107),
    ('byPicDataType', BYTE),
    ('sPicDataPath', c_char * 256),
])

NET_DVR_VEHICLE_RECOG_CFG = struct_tagNET_DVR_VEHICLE_RECOG_CFG
LPNET_DVR_VEHICLE_RECOG_CFG = POINTER(struct_tagNET_DVR_VEHICLE_RECOG_CFG)
tagNET_DVR_VEHICLE_RECOG_CFG = struct_tagNET_DVR_VEHICLE_RECOG_CFG
