from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_dvr_vehicle_info import NET_DVR_VEHICLE_INFO


class struct_tagNET_DVR_PLATE_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_PLATE_RESULT, [
    ('dwSize', DWORD),
    ('byResultType', BYTE),
    ('byChanIndex', BYTE),
    ('wAlarmRecordID', WORD),
    ('dwRelativeTime', DWORD),
    ('byAbsTime', BYTE * 32),
    ('dwPicLen', DWORD),
    ('dwPicPlateLen', DWORD),
    ('dwVideoLen', DWORD),
    ('byTrafficLight', BYTE),
    ('byPicNum', BYTE),
    ('byDriveChan', BYTE),
    ('byVehicleType', BYTE),
    ('dwBinPicLen', DWORD),
    ('dwCarPicLen', DWORD),
    ('dwFarCarPicLen', DWORD),
    ('pBuffer3', POINTER(BYTE)),
    ('pBuffer4', POINTER(BYTE)),
    ('pBuffer5', POINTER(BYTE)),
    ('byRelaLaneDirectionType', BYTE),
    ('byCarDirectionType', BYTE),
    ('byRes3', BYTE * 6),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('struVehicleInfo', NET_DVR_VEHICLE_INFO),
    ('pBuffer1', POINTER(BYTE)),
    ('pBuffer2', POINTER(BYTE)),
])

NET_DVR_PLATE_RESULT = struct_tagNET_DVR_PLATE_RESULT
LPNET_DVR_PLATE_RESULT = POINTER(struct_tagNET_DVR_PLATE_RESULT)
tagNET_DVR_PLATE_RESULT = struct_tagNET_DVR_PLATE_RESULT
