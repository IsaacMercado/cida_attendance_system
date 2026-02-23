from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRANS_AUDIO_INFO(Structure):
    pass

_S(struct_tagNET_DVR_TRANS_AUDIO_INFO, [
    ('dwSize', DWORD),
    ('sAudioName', c_char * 32),
    ('byAudioFormat', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_TRANS_AUDIO_INFO = struct_tagNET_DVR_TRANS_AUDIO_INFO
LPNET_DVR_TRANS_AUDIO_INFO = POINTER(struct_tagNET_DVR_TRANS_AUDIO_INFO)
tagNET_DVR_TRANS_AUDIO_INFO = struct_tagNET_DVR_TRANS_AUDIO_INFO
