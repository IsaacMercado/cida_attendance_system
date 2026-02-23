from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_relay_param import NET_DVR_RELAY_PARAM
from .net_dvr_vehicle_control import NET_DVR_VEHICLE_CONTROL


class struct_tagNET_DVR_ENTRANCE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ENTRANCE_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byBarrierGateCtrlMode', BYTE),
    ('byRes1', BYTE * 2),
    ('dwRelateTriggerMode', DWORD),
    ('dwMatchContent', DWORD),
    ('struRelayRelateInfo', NET_DVR_RELAY_PARAM * 12),
    ('byGateSingleIO', BYTE * 8),
    ('struVehicleCtrl', NET_DVR_VEHICLE_CONTROL * 8),
    ('byNotCloseCarFollow', BYTE),
    ('byParkingDetectEnabled', BYTE),
    ('byParkingDetectJudgeTime', BYTE),
    ('byRes2', BYTE * 61),
])

NET_DVR_ENTRANCE_CFG = struct_tagNET_DVR_ENTRANCE_CFG
LPNET_DVR_ENTRANCE_CFG = POINTER(struct_tagNET_DVR_ENTRANCE_CFG)
tagNET_DVR_ENTRANCE_CFG = struct_tagNET_DVR_ENTRANCE_CFG
