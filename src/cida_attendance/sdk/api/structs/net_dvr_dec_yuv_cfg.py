from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEC_YUV_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DEC_YUV_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwYUVAddress', DWORD * 3),
    ('wWidth', WORD),
    ('wHeight', WORD),
    ('byEnableAudio', BYTE),
    ('byRes2', BYTE * 3),
    ('dwAudioAddr', DWORD),
    ('byRes3', BYTE * 16),
])

NET_DVR_DEC_YUV_CFG = struct_tagNET_DVR_DEC_YUV_CFG
LPNET_DVR_DEC_YUV_CFG = POINTER(struct_tagNET_DVR_DEC_YUV_CFG)
tagNET_DVR_DEC_YUV_CFG = struct_tagNET_DVR_DEC_YUV_CFG
