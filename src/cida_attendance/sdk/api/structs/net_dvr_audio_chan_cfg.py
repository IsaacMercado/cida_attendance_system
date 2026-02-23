from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pu_stream_cfg_v41 import NET_DVR_PU_STREAM_CFG_V41


class struct_tagNET_DVR_AUDIO_CHAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_CHAN_CFG, [
    ('dwSize', DWORD),
    ('sChanName', BYTE * 32),
    ('byEnable', BYTE),
    ('byAudioSwitchType', BYTE),
    ('byRes', BYTE * 2),
    ('struAudioSrcInfo', NET_DVR_PU_STREAM_CFG_V41),
    ('dwWindowNo', DWORD),
    ('byRes2', BYTE * 28),
])

NET_DVR_AUDIO_CHAN_CFG = struct_tagNET_DVR_AUDIO_CHAN_CFG
LPNET_DVR_AUDIO_CHAN_CFG = POINTER(struct_tagNET_DVR_AUDIO_CHAN_CFG)
tagNET_DVR_AUDIO_CHAN_CFG = struct_tagNET_DVR_AUDIO_CHAN_CFG
