from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40


class struct_tagNET_DVR_VQD_LOOP_DIAGNOSE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VQD_LOOP_DIAGNOSE_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byVQDTypeEnable', BYTE * 32),
    ('byThresholdValue', BYTE * 32),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V40),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHolidayAlarmTime', NET_DVR_SCHEDTIME * 8),
    ('byRes', BYTE * 324),
])

NET_DVR_VQD_LOOP_DIAGNOSE_CFG = struct_tagNET_DVR_VQD_LOOP_DIAGNOSE_CFG
LPNET_DVR_VQD_LOOP_DIAGNOSE_CFG = POINTER(struct_tagNET_DVR_VQD_LOOP_DIAGNOSE_CFG)
tagNET_DVR_VQD_LOOP_DIAGNOSE_CFG = struct_tagNET_DVR_VQD_LOOP_DIAGNOSE_CFG
