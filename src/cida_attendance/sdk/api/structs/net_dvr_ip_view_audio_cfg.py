from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IP_VIEW_AUDIO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_IP_VIEW_AUDIO_CFG, [
    ('dwSize', DWORD),
    ('byAudioEncPri1', BYTE),
    ('byAudioEncPri2', BYTE),
    ('wAudioPacketLen1', WORD),
    ('wAudioPacketLen2', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_IP_VIEW_AUDIO_CFG = struct_tagNET_DVR_IP_VIEW_AUDIO_CFG
LPNET_DVR_IP_VIEW_AUDIO_CFG = POINTER(struct_tagNET_DVR_IP_VIEW_AUDIO_CFG)
tagNET_DVR_IP_VIEW_AUDIO_CFG = struct_tagNET_DVR_IP_VIEW_AUDIO_CFG
