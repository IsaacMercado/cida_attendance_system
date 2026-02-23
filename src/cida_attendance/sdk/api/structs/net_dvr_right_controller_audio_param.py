from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM, [
    ('dwSize', DWORD),
    ('dwFileSize', DWORD),
    ('dwAudioID', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM = struct_tagNET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM
LPNET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM = POINTER(struct_tagNET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM)
tagNET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM = struct_tagNET_DVR_RIGHT_CONTROLLER_AUDIO_PARAM
