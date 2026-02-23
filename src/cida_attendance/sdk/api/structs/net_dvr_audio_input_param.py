from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_INPUT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_INPUT_PARAM, [
    ('byAudioInputType', BYTE),
    ('byVolume', BYTE),
    ('byEnableNoiseFilter', BYTE),
    ('byres', BYTE * 5),
])

NET_DVR_AUDIO_INPUT_PARAM = struct_tagNET_DVR_AUDIO_INPUT_PARAM
LPNET_DVR_AUDIO_INPUT_PARAM = POINTER(struct_tagNET_DVR_AUDIO_INPUT_PARAM)
tagNET_DVR_AUDIO_INPUT_PARAM = struct_tagNET_DVR_AUDIO_INPUT_PARAM
