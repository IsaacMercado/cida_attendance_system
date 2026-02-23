from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_VEHICLE_RECOG_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_RECOG_RESULT, [
    ('dwSize', DWORD),
    ('sDataIndex', c_char * 64),
    ('wTaskNo', WORD),
    ('byRes', BYTE * 2),
    ('struPlateRect', NET_VCA_RECT),
    ('sLicense', c_char * 16),
    ('byVehicleType', BYTE),
    ('byColorDepth', BYTE),
    ('byColor', BYTE),
    ('byVehicleLogoRecog', BYTE),
    ('byVehicleSubLogoRecog', BYTE),
    ('byPilotSafebelt', BYTE),
    ('byCopilotSafebelt', BYTE),
    ('byPilotSunVisor', BYTE),
    ('byCopilotSunVisor', BYTE),
    ('byVehicleModel', BYTE),
    ('wVehicleLogoRecog', WORD),
    ('byRes1', BYTE * 251),
    ('byDataType', BYTE),
    ('dwPicType', DWORD),
    ('pVehicleBuffer', POINTER(BYTE)),
    ('dwVehicleBufferLen', DWORD),
    ('pPlateBuffer', POINTER(BYTE)),
    ('dwPlateBufferLen', DWORD),
    ('pPilotFaceBuffer', POINTER(BYTE)),
    ('dwPilotFaceBufferLen', DWORD),
    ('pCopilotFaceBuffer', POINTER(BYTE)),
    ('dwCopilotFaceBufferLen', DWORD),
    ('pPilotSafebeltBuffer', POINTER(BYTE)),
    ('dwPilotSafebeltBufferLen', DWORD),
    ('pCopilotSafebeltBuffer', POINTER(BYTE)),
    ('dwCopilotSafebeltBufferLen', DWORD),
    ('struVehicleRect', NET_VCA_RECT),
    ('struPilotRect', NET_VCA_RECT),
    ('struCopilotRect', NET_VCA_RECT),
    ('pJsonBuffer', POINTER(BYTE)),
    ('dwJsonBufferLen', DWORD),
    ('dwPostID', DWORD),
    ('struPostTime', NET_DVR_TIME_V30),
    ('Res2', BYTE * 56),
])

NET_DVR_VEHICLE_RECOG_RESULT = struct_tagNET_DVR_VEHICLE_RECOG_RESULT
LPNET_DVR_VEHICLE_RECOG_RESULT = POINTER(struct_tagNET_DVR_VEHICLE_RECOG_RESULT)
tagNET_DVR_VEHICLE_RECOG_RESULT = struct_tagNET_DVR_VEHICLE_RECOG_RESULT
