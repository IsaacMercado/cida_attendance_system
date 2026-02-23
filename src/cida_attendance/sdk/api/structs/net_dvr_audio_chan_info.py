from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_CHAN_INFO, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 48),
])

NET_DVR_AUDIO_CHAN_INFO = struct_tagNET_DVR_AUDIO_CHAN_INFO
LPNET_DVR_AUDIO_CHAN_INFO = POINTER(struct_tagNET_DVR_AUDIO_CHAN_INFO)
tagNET_DVR_AUDIO_CHAN_INFO = struct_tagNET_DVR_AUDIO_CHAN_INFO
