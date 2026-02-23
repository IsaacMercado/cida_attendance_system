from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LEDDISPLAY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LEDDISPLAY_CFG, [
    ('dwSize', DWORD),
    ('sDisplayInfo', c_char * 512),
    ('byDisplayMode', BYTE),
    ('bySpeedType', BYTE),
    ('byShowPlateEnable', BYTE),
    ('byRes1', BYTE),
    ('dwShowTime', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_LEDDISPLAY_CFG = struct_tagNET_DVR_LEDDISPLAY_CFG
LPNET_DVR_LEDDISPLAY_CFG = POINTER(struct_tagNET_DVR_LEDDISPLAY_CFG)
tagNET_DVR_LEDDISPLAY_CFG = struct_tagNET_DVR_LEDDISPLAY_CFG
