from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LCD_AUDIO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LCD_AUDIO_CFG, [
    ('dwSize', DWORD),
    ('byMute', BYTE),
    ('byVolume', BYTE),
    ('byBalance', c_char),
    ('byRes', BYTE * 33),
])

NET_DVR_LCD_AUDIO_CFG = struct_tagNET_DVR_LCD_AUDIO_CFG
LPNET_DVR_LCD_AUDIO_CFG = POINTER(struct_tagNET_DVR_LCD_AUDIO_CFG)
tagNET_DVR_LCD_AUDIO_CFG = struct_tagNET_DVR_LCD_AUDIO_CFG
