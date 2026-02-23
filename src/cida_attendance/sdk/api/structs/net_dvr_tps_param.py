from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TPS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TPS_PARAM, [
    ('byStart', BYTE),
    ('byCMD', BYTE),
    ('wSpaceHeadway', WORD),
    ('wDeviceID', WORD),
    ('wDataLen', WORD),
    ('byLane', BYTE),
    ('bySpeed', BYTE),
    ('byLaneState', BYTE),
    ('byQueueLen', BYTE),
    ('wLoopState', WORD),
    ('wStateMask', WORD),
    ('dwDownwardFlow', DWORD),
    ('dwUpwardFlow', DWORD),
    ('byJamLevel', BYTE),
    ('byVehicleDirection', BYTE),
    ('byJamFlow', BYTE),
    ('byChannelizationLane', BYTE),
    ('byVehicleType', BYTE),
    ('byRes1', BYTE * 5),
    ('wTimeHeadway', WORD),
])

NET_DVR_TPS_PARAM = struct_tagNET_DVR_TPS_PARAM
LPNET_DVR_TPS_PARAM = POINTER(struct_tagNET_DVR_TPS_PARAM)
tagNET_DVR_TPS_PARAM = struct_tagNET_DVR_TPS_PARAM
