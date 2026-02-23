from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_CONTENT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_CONTENT_CFG, [
    ('dwSize', DWORD),
    ('sLEDContent', BYTE * 512),
    ('byContentAct', BYTE),
    ('byContentSpeed', BYTE),
    ('byContentStayTime', BYTE),
    ('byRes', BYTE * 33),
])

NET_DVR_LED_CONTENT_CFG = struct_tagNET_DVR_LED_CONTENT_CFG
LPNET_DVR_LED_CONTENT_CFG = POINTER(struct_tagNET_DVR_LED_CONTENT_CFG)
tagNET_DVR_LED_CONTENT_CFG = struct_tagNET_DVR_LED_CONTENT_CFG
