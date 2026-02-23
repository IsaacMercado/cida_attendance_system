from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__tagNET_ITS_PASSVEHICLE_COST_ITEM(Structure):
    pass

_S(struct__tagNET_ITS_PASSVEHICLE_COST_ITEM, [
    ('dwSize', DWORD),
    ('dwPassVehicleID', DWORD),
    ('byIntime', BYTE * 32),
    ('byOuttime', BYTE * 32),
    ('byCardNo', BYTE * 24),
    ('byPlateInfo', BYTE * 16),
    ('fPayCost', c_float),
    ('byOperatorName', BYTE * 32),
    ('byVehicleType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPayRuleID', DWORD),
    ('dwFreeRuleID', DWORD),
    ('byRes2', BYTE * 256),
])

NET_ITS_PASSVEHICLE_COST_ITEM = struct__tagNET_ITS_PASSVEHICLE_COST_ITEM
LPNET_ITS_PASSVEHICLE_COST_ITEM = POINTER(struct__tagNET_ITS_PASSVEHICLE_COST_ITEM)
_tagNET_ITS_PASSVEHICLE_COST_ITEM = struct__tagNET_ITS_PASSVEHICLE_COST_ITEM
