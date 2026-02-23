from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_COMPRESSION_AUDIO(Structure):
    pass

_S(struct_tagNET_DVR_COMPRESSION_AUDIO, [
    ('byAudioEncType', BYTE),
    ('byAudioSamplingRate', BYTE),
    ('byAudioBitRate', BYTE),
    ('byres', BYTE * 4),
    ('bySupport', BYTE),
])

NET_DVR_COMPRESSION_AUDIO = struct_tagNET_DVR_COMPRESSION_AUDIO
LPNET_DVR_COMPRESSION_AUDIO = POINTER(struct_tagNET_DVR_COMPRESSION_AUDIO)
tagNET_DVR_COMPRESSION_AUDIO = struct_tagNET_DVR_COMPRESSION_AUDIO
