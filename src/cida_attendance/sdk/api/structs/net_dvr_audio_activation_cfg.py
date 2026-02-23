from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_ACTIVATION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_ACTIVATION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwChanNo', DWORD),
    ('bySensitivity', BYTE),
    ('byPriority', BYTE),
    ('wDelayTime', WORD),
    ('byRes2', BYTE),
    ('byEnablePreset', BYTE),
    ('wPreset', WORD),
    ('wBase', WORD),
    ('byRes3', BYTE * 2),
    ('byVoChanNo', BYTE * 9),
    ('byRes', BYTE * 255),
])

NET_DVR_AUDIO_ACTIVATION_CFG = struct_tagNET_DVR_AUDIO_ACTIVATION_CFG
LPNET_DVR_AUDIO_ACTIVATION_CFG = POINTER(struct_tagNET_DVR_AUDIO_ACTIVATION_CFG)
tagNET_DVR_AUDIO_ACTIVATION_CFG = struct_tagNET_DVR_AUDIO_ACTIVATION_CFG
