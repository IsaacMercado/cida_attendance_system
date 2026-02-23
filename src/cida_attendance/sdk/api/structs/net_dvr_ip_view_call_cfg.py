from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IP_VIEW_CALL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_IP_VIEW_CALL_CFG, [
    ('dwSize', DWORD),
    ('byEnableAutoResponse', BYTE),
    ('byAudoResponseTime', BYTE),
    ('byRes1', BYTE * 2),
    ('byEnableAlarmNumber1', BYTE),
    ('byRes2', BYTE * 3),
    ('byAlarmNumber1', BYTE * 32),
    ('byEnableAlarmNumber2', BYTE),
    ('byRes3', BYTE * 3),
    ('byAlarmNumber2', BYTE * 32),
    ('byRes4', BYTE * 72),
])

NET_DVR_IP_VIEW_CALL_CFG = struct_tagNET_DVR_IP_VIEW_CALL_CFG
LPNET_DVR_IP_VIEW_CALL_CFG = POINTER(struct_tagNET_DVR_IP_VIEW_CALL_CFG)
tagNET_DVR_IP_VIEW_CALL_CFG = struct_tagNET_DVR_IP_VIEW_CALL_CFG
