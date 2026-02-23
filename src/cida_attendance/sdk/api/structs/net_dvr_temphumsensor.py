from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEMPHUMSENSOR(Structure):
    pass

_S(struct_tagNET_DVR_TEMPHUMSENSOR, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byCtrlMode', BYTE),
    ('byTemperatureValue', BYTE),
    ('byHumidityValue', BYTE),
    ('byFanSwitch', BYTE),
    ('byThermometryUnit', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_TEMPHUMSENSOR = struct_tagNET_DVR_TEMPHUMSENSOR
LPNET_DVR_TEMPHUMSENSOR = POINTER(struct_tagNET_DVR_TEMPHUMSENSOR)
tagNET_DVR_TEMPHUMSENSOR = struct_tagNET_DVR_TEMPHUMSENSOR
