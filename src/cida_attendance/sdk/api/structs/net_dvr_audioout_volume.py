from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIOOUT_VOLUME(Structure):
    pass

_S(struct_tagNET_DVR_AUDIOOUT_VOLUME, [
    ('dwSize', DWORD),
    ('byAudioOutVolume', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_AUDIOOUT_VOLUME = struct_tagNET_DVR_AUDIOOUT_VOLUME
LPNET_DVR_AUDIOOUT_VOLUME = POINTER(struct_tagNET_DVR_AUDIOOUT_VOLUME)
tagNET_DVR_AUDIOOUT_VOLUME = struct_tagNET_DVR_AUDIOOUT_VOLUME
