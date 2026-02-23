from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_aid_info import NET_DVR_AID_INFO
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_dvr_scene_info import NET_DVR_SCENE_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_dvr_vehicle_info import NET_DVR_VEHICLE_INFO
from .net_its_picture_info import NET_ITS_PICTURE_INFO
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_TFS_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_TFS_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('dwIllegalType', DWORD),
    ('dwIllegalDuration', DWORD),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struSceneInfo', NET_DVR_SCENE_INFO),
    ('struBeginRecTime', NET_DVR_TIME_EX),
    ('struEndRecTime', NET_DVR_TIME_EX),
    ('struAIDInfo', NET_DVR_AID_INFO),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('struVehicleInfo', NET_DVR_VEHICLE_INFO),
    ('dwPicNum', DWORD),
    ('struPicInfo', NET_ITS_PICTURE_INFO * 8),
    ('bySpecificVehicleType', BYTE),
    ('byLaneNo', BYTE),
    ('wDevInfoIvmsChannelEx', WORD),
    ('struTime', NET_DVR_TIME_V30),
    ('dwSerialNo', DWORD),
    ('byVehicleAttribute', BYTE),
    ('byPilotSafebelt', BYTE),
    ('byCopilotSafebelt', BYTE),
    ('byPilotSunVisor', BYTE),
    ('byCopilotSunVisor', BYTE),
    ('byPilotCall', BYTE),
    ('byRes2', BYTE * 2),
    ('byIllegalCode', BYTE * 32),
    ('wCountry', WORD),
    ('byRegion', BYTE),
    ('byCrossLine', BYTE),
    ('byParkingSerialNO', BYTE * 16),
    ('byCrossSpaces', BYTE),
    ('byAngledParking', BYTE),
    ('byAlarmValidity', BYTE),
    ('byDoorsStatus', BYTE),
    ('dwXmlLen', DWORD),
    ('pXmlBuf', String),
    ('byVehicleHeadTailStatus', BYTE),
    ('byBrokenNetHttp', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_TFS_ALARM = struct_tagNET_DVR_TFS_ALARM
LPNET_DVR_TFS_ALARM = POINTER(struct_tagNET_DVR_TFS_ALARM)
tagNET_DVR_TFS_ALARM = struct_tagNET_DVR_TFS_ALARM
