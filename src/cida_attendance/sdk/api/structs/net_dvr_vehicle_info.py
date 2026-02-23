from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLE_INFO_(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_INFO_, [
    ('dwIndex', DWORD),
    ('byVehicleType', BYTE),
    ('byColorDepth', BYTE),
    ('byColor', BYTE),
    ('byRadarState', BYTE),
    ('wSpeed', WORD),
    ('wLength', WORD),
    ('byIllegalType', BYTE),
    ('byVehicleLogoRecog', BYTE),
    ('byVehicleSubLogoRecog', BYTE),
    ('byVehicleModel', BYTE),
    ('byCustomInfo', BYTE * 16),
    ('wVehicleLogoRecog', WORD),
    ('byIsParking', BYTE),
    ('byRes', BYTE),
    ('dwParkingTime', DWORD),
    ('byBelieve', BYTE),
    ('byCurrentWorkerNumber', BYTE),
    ('byCurrentGoodsLoadingRate', BYTE),
    ('byDoorsStatus', BYTE),
    ('byRes3', BYTE * 4),
])

NET_DVR_VEHICLE_INFO = struct_tagNET_DVR_VEHICLE_INFO_
LPNET_DVR_VEHICLE_INFO = POINTER(struct_tagNET_DVR_VEHICLE_INFO_)
tagNET_DVR_VEHICLE_INFO_ = struct_tagNET_DVR_VEHICLE_INFO_
