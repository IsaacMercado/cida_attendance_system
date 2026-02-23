from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_CHANNEL(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_CHANNEL, [
    ('dwChannelNum', DWORD),
    ('byres', BYTE * 32),
])

NET_DVR_AUDIO_CHANNEL = struct_tagNET_DVR_AUDIO_CHANNEL
LPNET_DVR_AUDIO_CHANNEL = POINTER(struct_tagNET_DVR_AUDIO_CHANNEL)
tagNET_DVR_AUDIO_CHANNEL = struct_tagNET_DVR_AUDIO_CHANNEL
