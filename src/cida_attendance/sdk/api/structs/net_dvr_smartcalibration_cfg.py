from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_smartcalibration_region import NET_DVR_SMARTCALIBRATION_REGION


class struct_tagNET_DVR_SMARTCALIBRATION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SMARTCALIBRATION_CFG, [
    ('dwSize', DWORD),
    ('bySmartType', BYTE),
    ('byRes', BYTE * 3),
    ('strRegion', NET_DVR_SMARTCALIBRATION_REGION * 128),
    ('byRes1', BYTE * 128),
])

NET_DVR_SMARTCALIBRATION_CFG = struct_tagNET_DVR_SMARTCALIBRATION_CFG
LPNET_DVR_SMARTCALIBRATION_CFG = POINTER(struct_tagNET_DVR_SMARTCALIBRATION_CFG)
tagNET_DVR_SMARTCALIBRATION_CFG = struct_tagNET_DVR_SMARTCALIBRATION_CFG
