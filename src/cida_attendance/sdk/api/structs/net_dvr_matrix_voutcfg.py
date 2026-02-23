from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_video_platform import NET_DVR_VIDEO_PLATFORM
from .net_dvr_videoeffect import NET_DVR_VIDEOEFFECT


class struct_tagNET_DVR_MATRIX_VOUTCFG(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_VOUTCFG, [
    ('dwSize', DWORD),
    ('byAudio', BYTE),
    ('byAudioWindowIdx', BYTE),
    ('byDispChanType', BYTE),
    ('byVedioFormat', BYTE),
    ('dwResolution', DWORD),
    ('dwWindowMode', DWORD),
    ('byJoinDecChan', BYTE * 36),
    ('byEnlargeStatus', BYTE),
    ('byEnlargeSubWindowIndex', BYTE),
    ('byScale', BYTE),
    ('byUnionType', BYTE),
    ('struDiff', NET_DVR_VIDEO_PLATFORM),
    ('dwDispChanNum', DWORD),
    ('wLEDWidth', WORD),
    ('wLEDHeight', WORD),
    ('byEnableVideoEffect', BYTE),
    ('byRes', BYTE * 3),
    ('struVideoEffect', NET_DVR_VIDEOEFFECT),
    ('byRes2', BYTE * 60),
])

NET_DVR_MATRIX_VOUTCFG = struct_tagNET_DVR_MATRIX_VOUTCFG
LPNET_DVR_MATRIX_VOUTCFG = POINTER(struct_tagNET_DVR_MATRIX_VOUTCFG)
tagNET_DVR_MATRIX_VOUTCFG = struct_tagNET_DVR_MATRIX_VOUTCFG
