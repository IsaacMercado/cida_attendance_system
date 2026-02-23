from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_PARAM, [
    ('dwSize', DWORD),
    ('byAudioFormat', BYTE),
    ('byRes1', BYTE),
    ('wChannels', WORD),
    ('dwSamplesPerSec', DWORD),
    ('byRes2', BYTE * 20),
    ('dwAudioSize', DWORD),
])

NET_DVR_AUDIO_PARAM = struct_tagNET_DVR_AUDIO_PARAM
LPNET_DVR_AUDIO_PARAM = POINTER(struct_tagNET_DVR_AUDIO_PARAM)
tagNET_DVR_AUDIO_PARAM = struct_tagNET_DVR_AUDIO_PARAM
