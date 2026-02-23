from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_NAME(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_NAME, [
    ('dwSize', DWORD),
    ('cName', c_char * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_AUDIO_NAME = struct_tagNET_DVR_AUDIO_NAME
LPNET_DVR_AUDIO_NAME = POINTER(struct_tagNET_DVR_AUDIO_NAME)
tagNET_DVR_AUDIO_NAME = struct_tagNET_DVR_AUDIO_NAME
