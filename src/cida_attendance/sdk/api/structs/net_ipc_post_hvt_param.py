from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_ipc_lane_hvt_param import NET_IPC_LANE_HVT_PARAM
from .net_itc_line import NET_ITC_LINE
from .net_itc_parking_detection import NET_ITC_PARKING_DETECTION
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_IPC_POST_HVT_PARAM(Structure):
    pass

_S(struct_tagNET_IPC_POST_HVT_PARAM, [
    ('byEnable', BYTE),
    ('byLaneNum', BYTE),
    ('byEnhancedMode', BYTE),
    ('byPicRecognition', BYTE),
    ('byRes', BYTE * 60),
    ('struLaneBoundaryLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struLaneParam', NET_IPC_LANE_HVT_PARAM * 6),
    ('szSceneName', c_char * 32),
    ('struSnapLine', NET_VCA_LINE),
    ('struParkingDetection', NET_ITC_PARKING_DETECTION),
    ('byRes1', BYTE * 328),
])

NET_IPC_POST_HVT_PARAM = struct_tagNET_IPC_POST_HVT_PARAM
LPNET_IPC_POST_HVT_PARAM = POINTER(struct_tagNET_IPC_POST_HVT_PARAM)
tagNET_IPC_POST_HVT_PARAM = struct_tagNET_IPC_POST_HVT_PARAM
