from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMALPOWER_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_THERMALPOWER_PARAM, [
    ('dwSize', DWORD),
    ('byPowerSwitch', BYTE),
    ('byRes', BYTE * 123),
])

NET_DVR_THERMALPOWER_PARAM = struct_tagNET_DVR_THERMALPOWER_PARAM
LPNET_DVR_THERMALPOWER_PARAM = POINTER(struct_tagNET_DVR_THERMALPOWER_PARAM)
tagNET_DVR_THERMALPOWER_PARAM = struct_tagNET_DVR_THERMALPOWER_PARAM
