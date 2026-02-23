from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_anti_sneak_reader_cfg import NET_DVR_ANTI_SNEAK_READER_CFG


class struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG, [
    ('dwSize', DWORD),
    ('struReaderCfg', NET_DVR_ANTI_SNEAK_READER_CFG * 16),
    ('byRes', BYTE * 128),
])

NET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG = struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG
LPNET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG = POINTER(struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG)
tagNET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG = struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_READERS_CFG
