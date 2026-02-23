from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_anti_sneak_host_info import NET_DVR_ANTI_SNEAK_HOST_INFO
from .net_dvr_anti_sneak_host_reader_info import NET_DVR_ANTI_SNEAK_HOST_READER_INFO


class struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struSneakHost', NET_DVR_ANTI_SNEAK_HOST_INFO * 8),
    ('struStartReader', NET_DVR_ANTI_SNEAK_HOST_READER_INFO),
    ('byRes2', BYTE * 128),
])

NET_DVR_ANTI_SNEAK_MULTI_HOST_CFG = struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_CFG
LPNET_DVR_ANTI_SNEAK_MULTI_HOST_CFG = POINTER(struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_CFG)
tagNET_DVR_ANTI_SNEAK_MULTI_HOST_CFG = struct_tagNET_DVR_ANTI_SNEAK_MULTI_HOST_CFG
