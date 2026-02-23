from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LASER_PARAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LASER_PARAM_CFG, [
    ('byControlMode', BYTE),
    ('bySensitivity', BYTE),
    ('byTriggerMode', BYTE),
    ('byBrightness', BYTE),
    ('byAngle', BYTE),
    ('byLimitBrightness', BYTE),
    ('byEnabled', BYTE),
    ('byIllumination', BYTE),
    ('byLightAngle', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_LASER_PARAM_CFG = struct_tagNET_DVR_LASER_PARAM_CFG
LPNET_DVR_LASER_PARAM_CFG = POINTER(struct_tagNET_DVR_LASER_PARAM_CFG)
tagNET_DVR_LASER_PARAM_CFG = struct_tagNET_DVR_LASER_PARAM_CFG
