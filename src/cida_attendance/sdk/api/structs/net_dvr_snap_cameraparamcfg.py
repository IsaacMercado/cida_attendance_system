from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_SNAP_CAMERAPARAMCFG(Structure):
    pass

_S(struct_tagNET_DVR_SNAP_CAMERAPARAMCFG, [
    ('byWDRMode', BYTE),
    ('byWDRType', BYTE),
    ('byWDRLevel', BYTE),
    ('byRes1', BYTE),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byDayNightBrightness', BYTE),
    ('byMCEEnabled', BYTE),
    ('byMCELevel', BYTE),
    ('byAutoContrastEnabled', BYTE),
    ('byAutoContrastLevel', BYTE),
    ('byLSEDetailEnabled', BYTE),
    ('byLSEDetailLevel', BYTE),
    ('byLPDEEnabled', BYTE),
    ('byLPDELevel', BYTE),
    ('byLseEnabled', BYTE),
    ('byLseLevel', BYTE),
    ('byLSEHaloLevel', BYTE),
    ('byLseType', BYTE),
    ('byRes2', BYTE * 3),
    ('struLSEStartTime', NET_DVR_TIME_EX),
    ('struLSEEndTime', NET_DVR_TIME_EX),
    ('byLightLevel', BYTE),
    ('byPlateContrastLevel', BYTE),
    ('byPlateSaturationLevel', BYTE),
    ('byRes', BYTE * 9),
])

NET_DVR_SNAP_CAMERAPARAMCFG = struct_tagNET_DVR_SNAP_CAMERAPARAMCFG
LPNET_DVR_SNAP_CAMERAPARAMCFG = POINTER(struct_tagNET_DVR_SNAP_CAMERAPARAMCFG)
tagNET_DVR_SNAP_CAMERAPARAMCFG = struct_tagNET_DVR_SNAP_CAMERAPARAMCFG
