from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FLASH_OUTCFG(Structure):
    pass

_S(struct_tagNET_DVR_FLASH_OUTCFG, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byRelatedIoIn', BYTE),
    ('byRecognizedLane', BYTE),
    ('byDetectBrightness', BYTE),
    ('byBrightnessThreld', BYTE),
    ('byStartHour', BYTE),
    ('byStartMinute', BYTE),
    ('byEndHour', BYTE),
    ('byEndMinute', BYTE),
    ('byFlashLightEnable', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_FLASH_OUTCFG = struct_tagNET_DVR_FLASH_OUTCFG
LPNET_DVR_FLASH_OUTCFG = POINTER(struct_tagNET_DVR_FLASH_OUTCFG)
tagNET_DVR_FLASH_OUTCFG = struct_tagNET_DVR_FLASH_OUTCFG
