from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GATE_TIME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_GATE_TIME_CFG, [
    ('dwSize', DWORD),
    ('dwHoldOnALarmTime', DWORD),
    ('dwHoldOnGateOpenTime', DWORD),
    ('dwPostponeIntrusionAlarmTime', DWORD),
    ('dwNoLaneAccessTimeLimitTime', DWORD),
    ('dwSafetyZoneStayTime', DWORD),
    ('byIRTriggerTimeoutTime', BYTE),
    ('byRes', BYTE * 299),
])

NET_DVR_GATE_TIME_CFG = struct_tagNET_DVR_GATE_TIME_CFG
LPNET_DVR_GATE_TIME_CFG = POINTER(struct_tagNET_DVR_GATE_TIME_CFG)
tagNET_DVR_GATE_TIME_CFG = struct_tagNET_DVR_GATE_TIME_CFG
