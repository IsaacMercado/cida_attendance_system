from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POSTEPOLICECFG(Structure):
    pass

_S(struct_tagNET_DVR_POSTEPOLICECFG, [
    ('dwSize', DWORD),
    ('dwDistance', DWORD),
    ('dwLightChan', DWORD * 6),
    ('byCapSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('byTrafficDirection', BYTE),
    ('byRes1', BYTE),
    ('wLoopPreDist', WORD),
    ('wTrigDelay', WORD),
    ('byRes', BYTE * 124),
])

NET_DVR_POSTEPOLICECFG = struct_tagNET_DVR_POSTEPOLICECFG
LPNET_DVR_POSTEPOLICECFG = POINTER(struct_tagNET_DVR_POSTEPOLICECFG)
tagNET_DVR_POSTEPOLICECFG = struct_tagNET_DVR_POSTEPOLICECFG
