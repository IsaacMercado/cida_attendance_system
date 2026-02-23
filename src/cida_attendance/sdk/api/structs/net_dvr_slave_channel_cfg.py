from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_slave_channel_param import NET_DVR_SLAVE_CHANNEL_PARAM


class struct_tagNET_DVR_SLAVE_CHANNEL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SLAVE_CHANNEL_CFG, [
    ('dwSize', DWORD),
    ('struChanParam', NET_DVR_SLAVE_CHANNEL_PARAM * 16),
    ('byRes', BYTE * 64),
])

NET_DVR_SLAVE_CHANNEL_CFG = struct_tagNET_DVR_SLAVE_CHANNEL_CFG
LPNET_DVR_SLAVE_CHANNEL_CFG = POINTER(struct_tagNET_DVR_SLAVE_CHANNEL_CFG)
tagNET_DVR_SLAVE_CHANNEL_CFG = struct_tagNET_DVR_SLAVE_CHANNEL_CFG
