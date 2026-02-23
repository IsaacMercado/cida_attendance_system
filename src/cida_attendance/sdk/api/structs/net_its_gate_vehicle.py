from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_dvr_vehicle_info import NET_DVR_VEHICLE_INFO
from .net_its_picture_info import NET_ITS_PICTURE_INFO


class struct_tagNET_ITS_GATE_VEHICLE(Structure):
    pass

_S(struct_tagNET_ITS_GATE_VEHICLE, [
    ('dwSize', DWORD),
    ('dwMatchNo', DWORD),
    ('byGroupNum', BYTE),
    ('byPicNo', BYTE),
    ('bySecondCam', BYTE),
    ('byRes', BYTE),
    ('wLaneid', WORD),
    ('byCamLaneId', BYTE),
    ('byRes1', BYTE),
    ('byAlarmReason', BYTE * 32),
    ('wBackList', WORD),
    ('wSpeedLimit', WORD),
    ('dwChanIndex', DWORD),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('struVehicleInfo', NET_DVR_VEHICLE_INFO),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('byDir', BYTE),
    ('byDetectType', BYTE),
    ('byRes2', BYTE * 2),
    ('byCardNo', BYTE * 48),
    ('dwPicNum', DWORD),
    ('struPicInfo', NET_ITS_PICTURE_INFO * 4),
    ('bySwipeTime', BYTE * 32),
    ('byRes3', BYTE * 224),
])

NET_ITS_GATE_VEHICLE = struct_tagNET_ITS_GATE_VEHICLE
LPNET_ITS_GATE_VEHICLE = POINTER(struct_tagNET_ITS_GATE_VEHICLE)
tagNET_ITS_GATE_VEHICLE = struct_tagNET_ITS_GATE_VEHICLE
