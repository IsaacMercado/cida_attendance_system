from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_DIACRITICAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_DIACRITICAL_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byBassValue', c_char),
    ('byRes', BYTE * 62),
])

NET_DVR_AUDIO_DIACRITICAL_CFG = struct_tagNET_DVR_AUDIO_DIACRITICAL_CFG
LPNET_DVR_AUDIO_DIACRITICAL_CFG = POINTER(struct_tagNET_DVR_AUDIO_DIACRITICAL_CFG)
tagNET_DVR_AUDIO_DIACRITICAL_CFG = struct_tagNET_DVR_AUDIO_DIACRITICAL_CFG
