from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subsystem_status import NET_DVR_SUBSYSTEM_STATUS


class struct_tagNET_DVR_MATRIX_SUBBOARD(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_SUBBOARD, [
    ('byBoardNo', BYTE),
    ('byPcieConnectStatus', BYTE),
    ('byRes', BYTE * 2),
    ('dwHardwareVersion', DWORD),
    ('dwPcieBandwidth', DWORD),
    ('dwTemperature', DWORD),
    ('struSubsystemStatus', NET_DVR_SUBSYSTEM_STATUS * 12),
    ('byRes2', BYTE * 16),
])

NET_DVR_MATRIX_SUBBOARD = struct_tagNET_DVR_MATRIX_SUBBOARD
LPNET_DVR_MATRIX_SUBBOARD = POINTER(struct_tagNET_DVR_MATRIX_SUBBOARD)
tagNET_DVR_MATRIX_SUBBOARD = struct_tagNET_DVR_MATRIX_SUBBOARD
