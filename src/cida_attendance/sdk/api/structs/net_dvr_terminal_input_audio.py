from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_howling_suppression import NET_DVR_HOWLING_SUPPRESSION


class struct_tagNET_DVR_TERMINAL_INPUT_AUDIO(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_INPUT_AUDIO, [
    ('dwChannel', DWORD),
    ('byGainType', BYTE),
    ('byEnableSimulate', BYTE),
    ('byVolumeSimulate', BYTE),
    ('byEnableDigital', BYTE),
    ('byVolumeDigital', BYTE),
    ('byRes1', BYTE * 3),
    ('struHsParam', NET_DVR_HOWLING_SUPPRESSION),
    ('byRes', BYTE * 604),
])

NET_DVR_TERMINAL_INPUT_AUDIO = struct_tagNET_DVR_TERMINAL_INPUT_AUDIO
LPNET_DVR_TERMINAL_INPUT_AUDIO = POINTER(struct_tagNET_DVR_TERMINAL_INPUT_AUDIO)
tagNET_DVR_TERMINAL_INPUT_AUDIO = struct_tagNET_DVR_TERMINAL_INPUT_AUDIO
