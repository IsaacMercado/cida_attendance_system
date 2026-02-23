from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_COLOR_TEMPERATURE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_COLOR_TEMPERATURE_CFG, [
    ('byRed', BYTE),
    ('byGreen', BYTE),
    ('byBlue', BYTE),
    ('byRedOffset', BYTE),
    ('byGreenOffset', BYTE),
    ('byBlueOffset', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_COLOR_TEMPERATURE_CFG = struct_tagNET_DVR_COLOR_TEMPERATURE_CFG
LPNET_DVR_COLOR_TEMPERATURE_CFG = POINTER(struct_tagNET_DVR_COLOR_TEMPERATURE_CFG)
tagNET_DVR_COLOR_TEMPERATURE_CFG = struct_tagNET_DVR_COLOR_TEMPERATURE_CFG
