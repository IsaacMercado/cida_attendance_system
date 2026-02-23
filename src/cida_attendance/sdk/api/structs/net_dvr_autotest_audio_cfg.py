from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUTOTEST_AUDIO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUTOTEST_AUDIO_CFG, [
    ('dwVoCh', DWORD),
    ('dwOpen', DWORD),
])

NET_DVR_AUTOTEST_AUDIO_CFG = struct_tagNET_DVR_AUTOTEST_AUDIO_CFG
LPNET_DVR_AUTOTEST_AUDIO_CFG = POINTER(struct_tagNET_DVR_AUTOTEST_AUDIO_CFG)
tagNET_DVR_AUTOTEST_AUDIO_CFG = struct_tagNET_DVR_AUTOTEST_AUDIO_CFG
