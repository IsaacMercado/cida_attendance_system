from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_address import NET_DVR_ADDRESS
from .net_dvr_encodeinfo import NET_DVR_ENCODEINFO
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_TRANSSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_TRANSSTATUS, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('byMode', BYTE),
    ('byLinkNums', BYTE),
    ('byPassiveTransMode', BYTE),
    ('byRes', BYTE),
    ('struDstIPInfo', NET_DVR_ADDRESS * 6),
    ('byTransResource', BYTE),
    ('byRes1', BYTE * 15),
    ('struSrcEncodeInfo', NET_DVR_ENCODEINFO),
    ('struDstEncodeInfo', NET_DVR_ENCODEINFO * 6),
    ('byRes2', BYTE * 36),
])

NET_DVR_TRANSSTATUS = struct_tagNET_DVR_TRANSSTATUS
LPNET_DVR_TRANSSTATUS = POINTER(struct_tagNET_DVR_TRANSSTATUS)
tagNET_DVR_TRANSSTATUS = struct_tagNET_DVR_TRANSSTATUS
