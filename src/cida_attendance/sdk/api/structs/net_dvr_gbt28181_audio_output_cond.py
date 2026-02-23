from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_COND(Structure):
    pass

_S(struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_COND, [
    ('dwSize', DWORD),
    ('dwAudioChannel', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_GBT28181_AUDIO_OUTPUT_COND = struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_COND
LPNET_DVR_GBT28181_AUDIO_OUTPUT_COND = POINTER(struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_COND)
tagNET_DVR_GBT28181_AUDIO_OUTPUT_COND = struct_tagNET_DVR_GBT28181_AUDIO_OUTPUT_COND
