from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_LED_AREA_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LED_AREA_INFO, [
    ('dwSize', DWORD),
    ('dwLEDAreaNo', DWORD),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('dwaOutputNo', DWORD * 512),
    ('byAreaType', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_LED_AREA_INFO = struct_tagNET_DVR_LED_AREA_INFO
LPNET_DVR_LED_AREA_INFO = POINTER(struct_tagNET_DVR_LED_AREA_INFO)
tagNET_DVR_LED_AREA_INFO = struct_tagNET_DVR_LED_AREA_INFO
