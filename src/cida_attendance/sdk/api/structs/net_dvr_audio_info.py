from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_INFO(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_INFO, [
    ('dwSize', DWORD),
    ('byAudioChanType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwAudioNo', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_AUDIO_INFO = struct_tagNET_DVR_AUDIO_INFO
LPNET_DVR_AUDIO_INFO = POINTER(struct_tagNET_DVR_AUDIO_INFO)
tagNET_DVR_AUDIO_INFO = struct_tagNET_DVR_AUDIO_INFO
