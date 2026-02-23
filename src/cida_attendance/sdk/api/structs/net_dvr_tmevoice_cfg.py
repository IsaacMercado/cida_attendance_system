from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TMEVOICE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TMEVOICE_CFG, [
    ('dwSize', DWORD),
    ('byVoiceSpeed', BYTE),
    ('byVoicePitch', BYTE),
    ('byVoiceVolum', BYTE),
    ('byVoicePlateEnable', BYTE),
    ('dwVoiceRole', DWORD),
    ('sInfo', c_char * 64),
    ('sFileName', c_char * 64),
    ('byRes', BYTE * 64),
])

NET_DVR_TMEVOICE_CFG = struct_tagNET_DVR_TMEVOICE_CFG
LPNET_DVR_TMEVOICE_CFG = POINTER(struct_tagNET_DVR_TMEVOICE_CFG)
tagNET_DVR_TMEVOICE_CFG = struct_tagNET_DVR_TMEVOICE_CFG
