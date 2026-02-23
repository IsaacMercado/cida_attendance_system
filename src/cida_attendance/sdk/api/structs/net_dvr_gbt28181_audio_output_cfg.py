from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_CFG, [
    ('dwSize', DWORD),
    ('szAudioOutNumID', c_char * 64),
    ('byRes', BYTE * 256),
])

NET_DVR_GBT28181_AUDIO_OUTPUT_CFG = struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_CFG
LPNET_DVR_GBT28181_AUDIO_OUTPUT_CFG = POINTER(struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_CFG)
tagNET_DVR_GBT28181_AUDIO_OUTPUT_CFG = struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_CFG
