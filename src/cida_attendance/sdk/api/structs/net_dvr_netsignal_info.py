from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_pu_stream_cfg import NET_DVR_PU_STREAM_CFG


class struct_tagNET_DVR_NETSIGNAL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_NETSIGNAL_INFO, [
    ('dwSize', DWORD),
    ('byDevName', BYTE * 32),
    ('struPuStream', NET_DVR_PU_STREAM_CFG),
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('sGroupName', BYTE * 32),
    ('wResolutionX', WORD),
    ('wResolutionY', WORD),
    ('byRes2', BYTE * 24),
])

NET_DVR_NETSIGNAL_INFO = struct_tagNET_DVR_NETSIGNAL_INFO
LPNET_DVR_NETSIGNAL_INFO = POINTER(struct_tagNET_DVR_NETSIGNAL_INFO)
tagNET_DVR_NETSIGNAL_INFO = struct_tagNET_DVR_NETSIGNAL_INFO
