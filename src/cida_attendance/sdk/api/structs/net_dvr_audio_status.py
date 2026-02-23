from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_STATUS, [
    ('byMute', BYTE),
    ('byVolume', BYTE),
    ('byAudioInputDisabled', BYTE),
    ('byAudioInputVolume', BYTE),
    ('byRes', BYTE * 32),
])

NET_DVR_AUDIO_STATUS = struct_tagNET_DVR_AUDIO_STATUS
LPNET_DVR_AUDIO_STATUS = POINTER(struct_tagNET_DVR_AUDIO_STATUS)
tagNET_DVR_AUDIO_STATUS = struct_tagNET_DVR_AUDIO_STATUS
