from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_EFFECTIVE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_EFFECTIVE_CFG, [
    ('dwSize', DWORD),
    ('dwCheckDelay', DWORD),
    ('byThreshold', BYTE),
    ('byVolumePercent', BYTE),
    ('byPriority', BYTE),
    ('byRes', BYTE * 301),
])

NET_DVR_AUDIO_EFFECTIVE_CFG = struct_tagNET_DVR_AUDIO_EFFECTIVE_CFG
LPNET_DVR_AUDIO_EFFECTIVE_CFG = POINTER(struct_tagNET_DVR_AUDIO_EFFECTIVE_CFG)
tagNET_DVR_AUDIO_EFFECTIVE_CFG = struct_tagNET_DVR_AUDIO_EFFECTIVE_CFG
