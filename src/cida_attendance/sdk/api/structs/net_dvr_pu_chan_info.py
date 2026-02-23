from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PU_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PU_CHAN_INFO, [
    ('struIpAddr', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('wChannel', WORD),
    ('byRes', BYTE * 24),
])

NET_DVR_PU_CHAN_INFO = struct_tagNET_DVR_PU_CHAN_INFO
LPNET_DVR_PU_CHAN_INFO = POINTER(struct_tagNET_DVR_PU_CHAN_INFO)
tagNET_DVR_PU_CHAN_INFO = struct_tagNET_DVR_PU_CHAN_INFO
