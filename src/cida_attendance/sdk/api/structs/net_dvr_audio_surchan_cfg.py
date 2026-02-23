from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_AUDIO_SURCHAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_SURCHAN_CFG, [
    ('dwSize', DWORD),
    ('byStatus', BYTE),
    ('byRes1', BYTE * 3),
    ('dwSubWinNum', DWORD),
    ('dwSurChanNum', DWORD),
    ('struIpaddr', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes2', BYTE * 14),
])

NET_DVR_AUDIO_SURCHAN_CFG = struct_tagNET_DVR_AUDIO_SURCHAN_CFG
LPNET_DVR_AUDIO_SURCHAN_CFG = POINTER(struct_tagNET_DVR_AUDIO_SURCHAN_CFG)
tagNET_DVR_AUDIO_SURCHAN_CFG = struct_tagNET_DVR_AUDIO_SURCHAN_CFG
