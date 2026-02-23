from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_channel_linkage_cfg import NET_DVR_SINGLE_CHANNEL_LINKAGE_CFG


class struct_tagNET_DVR_REGION_CHANNEL_LINKAGE_CFG_(Structure):
    pass

_S(struct_tagNET_DVR_REGION_CHANNEL_LINKAGE_CFG_, [
    ('dwSize', DWORD),
    ('struLinkChannels', NET_DVR_SINGLE_CHANNEL_LINKAGE_CFG * 4),
    ('byRes', BYTE * 64),
])

NET_DVR_ZONE_CHANNEL_LINKAGE_CFG = struct_tagNET_DVR_REGION_CHANNEL_LINKAGE_CFG_
LPNET_DVR_ZONE_CHANNEL_LINKAGE_CFG = POINTER(struct_tagNET_DVR_REGION_CHANNEL_LINKAGE_CFG_)
tagNET_DVR_REGION_CHANNEL_LINKAGE_CFG_ = struct_tagNET_DVR_REGION_CHANNEL_LINKAGE_CFG_
