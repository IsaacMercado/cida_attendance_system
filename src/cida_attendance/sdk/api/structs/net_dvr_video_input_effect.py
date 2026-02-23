from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_video_effect import NET_DVR_VIDEO_EFFECT


class struct_tagNET_DVR_VIDEO_INPUT_EFFECT(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INPUT_EFFECT, [
    ('dwSize', DWORD),
    ('wEffectMode', WORD),
    ('byRes1', BYTE * 146),
    ('struVideoEffect', NET_DVR_VIDEO_EFFECT),
    ('byRes2', BYTE * 60),
])

NET_DVR_VIDEO_INPUT_EFFECT = struct_tagNET_DVR_VIDEO_INPUT_EFFECT
LPNET_DVR_VIDEO_INPUT_EFFECT = POINTER(struct_tagNET_DVR_VIDEO_INPUT_EFFECT)
tagNET_DVR_VIDEO_INPUT_EFFECT = struct_tagNET_DVR_VIDEO_INPUT_EFFECT
