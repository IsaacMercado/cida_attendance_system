from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_dvr_vehicle_info import NET_DVR_VEHICLE_INFO
from .net_dvr_vehicle_weight_result import NET_DVR_VEHICLE_WEIGHT_RESULT
from .net_its_picture_info import NET_ITS_PICTURE_INFO


class struct_tagNET_DVR_PLATE_RESULT_V50(Structure):
    pass

_S(struct_tagNET_DVR_PLATE_RESULT_V50, [
    ('dwSize', DWORD),
    ('dwMatchNo', DWORD),
    ('byGroupNum', BYTE),
    ('byPicNo', BYTE),
    ('bySecondCam', BYTE),
    ('byFeaturePicNo', BYTE),
    ('byDriveChan', BYTE),
    ('byVehicleType', BYTE),
    ('byDetSceneID', BYTE),
    ('byVehicleAttribute', BYTE),
    ('wIllegalType', WORD),
    ('byIllegalSubType', BYTE * 8),
    ('byPostPicNo', BYTE),
    ('byChanIndex', BYTE),
    ('wSpeedLimit', WORD),
    ('byChanIndexEx', BYTE),
    ('byVehiclePositionControl', BYTE),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('struVehicleInfo', NET_DVR_VEHICLE_INFO),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('byDir', BYTE),
    ('byDetectType', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('byCarDirectionType', BYTE),
    ('dwCustomIllegalType', DWORD),
    ('pIllegalInfoBuf', POINTER(BYTE)),
    ('byIllegalFromatType', BYTE),
    ('byPendant', BYTE),
    ('byDataAnalysis', BYTE),
    ('byYellowLabelCar', BYTE),
    ('byDangerousVehicles', BYTE),
    ('byPilotSafebelt', BYTE),
    ('byCopilotSafebelt', BYTE),
    ('byPilotSunVisor', BYTE),
    ('byCopilotSunVisor', BYTE),
    ('byPilotCall', BYTE),
    ('byBarrierGateCtrlType', BYTE),
    ('byAlarmDataType', BYTE),
    ('struSnapFirstPicTime', NET_DVR_TIME_V30),
    ('dwIllegalTime', DWORD),
    ('dwPicNum', DWORD),
    ('struPicInfo', NET_ITS_PICTURE_INFO * 6),
    ('struWeightResult', NET_DVR_VEHICLE_WEIGHT_RESULT),
    ('byRes', BYTE * 256),
])

NET_DVR_PLATE_RESULT_V50 = struct_tagNET_DVR_PLATE_RESULT_V50
LPNET_DVR_PLATE_RESULT_V50 = POINTER(struct_tagNET_DVR_PLATE_RESULT_V50)
tagNET_DVR_PLATE_RESULT_V50 = struct_tagNET_DVR_PLATE_RESULT_V50
