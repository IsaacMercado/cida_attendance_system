from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_dvr_vehicle_info import NET_DVR_VEHICLE_INFO
from .net_its_picture_info import NET_ITS_PICTURE_INFO


class struct_tagNET_DVR_TME_VEHICLE_RESULT_(Structure):
    pass

_S(struct_tagNET_DVR_TME_VEHICLE_RESULT_, [
    ('dwSize', DWORD),
    ('wLaneid', WORD),
    ('byCamLaneId', BYTE),
    ('byRes1', BYTE),
    ('dwChanIndex', DWORD),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('struVehicleInfo', NET_DVR_VEHICLE_INFO),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('byDir', BYTE),
    ('byRes2', BYTE),
    ('wBackList', WORD),
    ('dwPicNum', DWORD),
    ('struPicInfo', NET_ITS_PICTURE_INFO * 4),
    ('byPassVehicleID', BYTE * 32),
    ('byCardNo', BYTE * 48),
    ('bySwipeTime', BYTE * 32),
    ('dwCharge', DWORD),
    ('byHistory', BYTE),
    ('byLetPass', BYTE),
    ('byRes3', BYTE * 186),
])

NET_DVR_TME_VEHICLE_RESULT = struct_tagNET_DVR_TME_VEHICLE_RESULT_
LPNET_DVR_TME_VEHICLE_RESULT = POINTER(struct_tagNET_DVR_TME_VEHICLE_RESULT_)
tagNET_DVR_TME_VEHICLE_RESULT_ = struct_tagNET_DVR_TME_VEHICLE_RESULT_
