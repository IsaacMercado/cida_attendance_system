from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VOLUME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VOLUME_CFG, [
    ('dwSize', DWORD),
    ('wVolume', WORD * 8),
    ('byPhantomPowerSupply', BYTE),
    ('byEnableAEC', BYTE),
    ('wTalkVolume', WORD),
    ('byEnableFBC', BYTE * 8),
    ('wVolumeEx', WORD * 8),
    ('byRes', BYTE * 4),
])

NET_DVR_VOLUME_CFG = struct_tagNET_DVR_VOLUME_CFG
LPNET_DVR_VOLUME_CFG = POINTER(struct_tagNET_DVR_VOLUME_CFG)
tagNET_DVR_VOLUME_CFG = struct_tagNET_DVR_VOLUME_CFG
