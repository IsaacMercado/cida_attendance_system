from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_matrix_subboard_v50 import NET_DVR_MATRIX_SUBBOARD_V50


class struct_tagNET_DVR_MATRIX_STATUS_V50(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_STATUS_V50, [
    ('dwSize', DWORD),
    ('byMainFrameType', BYTE),
    ('bySoltNum', BYTE),
    ('byBoardNum', BYTE),
    ('byLCDPanelStatus', BYTE),
    ('struMatrixSubboard', NET_DVR_MATRIX_SUBBOARD_V50 * 16),
    ('dwFanSequence', DWORD),
    ('dwFanConnectStatus', DWORD),
    ('dwFanOperationStatus', DWORD),
    ('byDeviceModel', BYTE * 32),
    ('byPowerNums', BYTE),
    ('byMainBoardNums', BYTE),
    ('byHotStandbyMode', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_MATRIX_STATUS_V50 = struct_tagNET_DVR_MATRIX_STATUS_V50
LPNET_DVR_MATRIX_STATUS_V50 = POINTER(struct_tagNET_DVR_MATRIX_STATUS_V50)
tagNET_DVR_MATRIX_STATUS_V50 = struct_tagNET_DVR_MATRIX_STATUS_V50
