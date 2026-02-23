from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_AUDIO_ABNORMAL(Structure):
    pass

_S(struct_tagNET_VCA_AUDIO_ABNORMAL, [
    ('wDecibel', WORD),
    ('bySensitivity', BYTE),
    ('byAudioMode', BYTE),
    ('byEnable', BYTE),
    ('byThreshold', BYTE),
    ('byRes', BYTE * 54),
])

NET_VCA_AUDIO_ABNORMAL = struct_tagNET_VCA_AUDIO_ABNORMAL
LPNET_VCA_AUDIO_ABNORMAL = POINTER(struct_tagNET_VCA_AUDIO_ABNORMAL)
tagNET_VCA_AUDIO_ABNORMAL = struct_tagNET_VCA_AUDIO_ABNORMAL
