from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_OUTPUT_PORT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_OUTPUT_PORT_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPortNum', DWORD),
    ('dwPortNo', DWORD * 32),
    ('byRes2', BYTE * 64),
])

NET_DVR_LED_OUTPUT_PORT_CFG = struct_tagNET_DVR_LED_OUTPUT_PORT_CFG
LPNET_DVR_LED_OUTPUT_PORT_CFG = POINTER(struct_tagNET_DVR_LED_OUTPUT_PORT_CFG)
tagNET_DVR_LED_OUTPUT_PORT_CFG = struct_tagNET_DVR_LED_OUTPUT_PORT_CFG
