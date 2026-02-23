from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subsystem_status import NET_DVR_SUBSYSTEM_STATUS


class struct_tagNET_DVR_MATRIX_SUBBOARD_V50(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_SUBBOARD_V50, [
    ('byBoardNo', BYTE),
    ('byPcieConnectStatus', BYTE),
    ('byRes', BYTE),
    ('byTemperatureAlarm', BYTE),
    ('dwHardwareVersion', DWORD),
    ('dwPcieBandwidth', DWORD),
    ('dwTemperature', DWORD),
    ('struSubsystemStatus', NET_DVR_SUBSYSTEM_STATUS * 12),
    ('bySubboardModel', BYTE * 32),
    ('byRes1', BYTE * 32),
])

NET_DVR_MATRIX_SUBBOARD_V50 = struct_tagNET_DVR_MATRIX_SUBBOARD_V50
LPNET_DVR_MATRIX_SUBBOARD_V50 = POINTER(struct_tagNET_DVR_MATRIX_SUBBOARD_V50)
tagNET_DVR_MATRIX_SUBBOARD_V50 = struct_tagNET_DVR_MATRIX_SUBBOARD_V50
