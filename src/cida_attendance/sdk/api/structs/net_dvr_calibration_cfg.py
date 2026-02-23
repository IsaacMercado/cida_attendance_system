from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_calibration_prarm_union import NET_DVR_CALIBRATION_PRARM_UNION


class struct_tagNET_DVR_CALIBRATION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CALIBRATION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byCalibrationType', BYTE),
    ('byRes1', BYTE * 2),
    ('uCalibrateParam', NET_DVR_CALIBRATION_PRARM_UNION),
    ('byRes2', BYTE * 12),
])

NET_DVR_CALIBRATION_CFG = struct_tagNET_DVR_CALIBRATION_CFG
LPNET_DVR_CALIBRATION_CFG = POINTER(struct_tagNET_DVR_CALIBRATION_CFG)
tagNET_DVR_CALIBRATION_CFG = struct_tagNET_DVR_CALIBRATION_CFG
