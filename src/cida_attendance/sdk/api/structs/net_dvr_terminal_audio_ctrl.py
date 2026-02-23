from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TERMINAL_AUDIO_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_AUDIO_CTRL, [
    ('byMute', BYTE),
    ('byVolume', BYTE),
    ('byAudioInputDisabled', BYTE),
    ('byAudioInputVolume', BYTE),
    ('byRes', BYTE * 636),
])

NET_DVR_TERMINAL_AUDIO_CTRL = struct_tagNET_DVR_TERMINAL_AUDIO_CTRL
LPNET_DVR_TERMINAL_AUDIO_CTRL = POINTER(struct_tagNET_DVR_TERMINAL_AUDIO_CTRL)
tagNET_DVR_TERMINAL_AUDIO_CTRL = struct_tagNET_DVR_TERMINAL_AUDIO_CTRL
