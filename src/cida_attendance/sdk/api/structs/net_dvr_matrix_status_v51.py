from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_matrix_subboard_v51 import NET_DVR_MATRIX_SUBBOARD_V51


class struct_tagNET_DVR_MATRIX_STATUS_V51(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_STATUS_V51, [
    ('dwSize', DWORD),
    ('byMainFrameType', BYTE),
    ('bySoltNum', BYTE),
    ('byBoardNum', BYTE),
    ('byLCDPanelStatus', BYTE),
    ('struMatrixSubboard', NET_DVR_MATRIX_SUBBOARD_V51 * 32),
    ('dwFanSequence', DWORD),
    ('dwFanConnectStatus', DWORD),
    ('dwFanOperationStatus', DWORD),
    ('byDeviceModel', BYTE * 32),
    ('byFanSpeed', BYTE * 32),
    ('byMainMemUsed', BYTE),
    ('byMainCpuUsed', BYTE),
    ('byNetwordUsed', BYTE),
    ('byRes1', BYTE),
    ('dwMainSoftwareVer', DWORD),
    ('byPowerNums', BYTE),
    ('byMainBoardNums', BYTE),
    ('byHotStandbyMode', BYTE),
    ('byRes2', BYTE * 125),
])

NET_DVR_MATRIX_STATUS_V51 = struct_tagNET_DVR_MATRIX_STATUS_V51
LPNET_DVR_MATRIX_STATUS_V51 = POINTER(struct_tagNET_DVR_MATRIX_STATUS_V51)
tagNET_DVR_MATRIX_STATUS_V51 = struct_tagNET_DVR_MATRIX_STATUS_V51
