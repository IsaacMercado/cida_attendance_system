from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_dvr_vehicle_info import NET_DVR_VEHICLE_INFO
from .net_its_picture_info import NET_ITS_PICTURE_INFO


class struct__tagNET_ITS_PARK_VEHICLE_(Structure):
    pass

_S(struct__tagNET_ITS_PARK_VEHICLE_, [
    ('dwSize', DWORD),
    ('byGroupNum', BYTE),
    ('byPicNo', BYTE),
    ('byLocationNum', BYTE),
    ('byParkError', BYTE),
    ('byParkingNo', BYTE * 16),
    ('byLocationStatus', BYTE),
    ('bylogicalLaneNum', BYTE),
    ('wUpLoadType', WORD),
    ('byRes1', BYTE * 4),
    ('dwChanIndex', DWORD),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('struVehicleInfo', NET_DVR_VEHICLE_INFO),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('dwPicNum', DWORD),
    ('struPicInfo', NET_ITS_PICTURE_INFO * 2),
    ('byRes2', BYTE * 256),
])

NET_ITS_PARK_VEHICLE = struct__tagNET_ITS_PARK_VEHICLE_
LPNET_ITS_PARK_VEHICLE = POINTER(struct__tagNET_ITS_PARK_VEHICLE_)
_tagNET_ITS_PARK_VEHICLE_ = struct__tagNET_ITS_PARK_VEHICLE_
