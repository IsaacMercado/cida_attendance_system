from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_address import NET_DVR_ADDRESS


class struct_tagNET_DVR_ANTI_SNEAK_HOST_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ANTI_SNEAK_HOST_INFO, [
    ('struDVRIP', NET_DVR_ADDRESS),
    ('byIsStartAddr', BYTE),
    ('byHostNo', BYTE),
    ('byRes', BYTE * 34),
])

NET_DVR_ANTI_SNEAK_HOST_INFO = struct_tagNET_DVR_ANTI_SNEAK_HOST_INFO
LPNET_DVR_ANTI_SNEAK_HOST_INFO = POINTER(struct_tagNET_DVR_ANTI_SNEAK_HOST_INFO)
tagNET_DVR_ANTI_SNEAK_HOST_INFO = struct_tagNET_DVR_ANTI_SNEAK_HOST_INFO
