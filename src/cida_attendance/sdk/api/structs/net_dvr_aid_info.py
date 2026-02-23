from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_direction import NET_DVR_DIRECTION


class struct_tagNET_DVR_AID_INFO(Structure):
    pass

_S(struct_tagNET_DVR_AID_INFO, [
    ('byRuleID', BYTE),
    ('byVisibilityLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('byRuleName', BYTE * 32),
    ('dwAIDType', DWORD),
    ('struDirect', NET_DVR_DIRECTION),
    ('bySpeedLimit', BYTE),
    ('byCurrentSpeed', BYTE),
    ('byVehicleEnterState', BYTE),
    ('byState', BYTE),
    ('byParkingID', BYTE * 16),
    ('dwAIDTypeEx', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_AID_INFO = struct_tagNET_DVR_AID_INFO
LPNET_DVR_AID_INFO = POINTER(struct_tagNET_DVR_AID_INFO)
tagNET_DVR_AID_INFO = struct_tagNET_DVR_AID_INFO
