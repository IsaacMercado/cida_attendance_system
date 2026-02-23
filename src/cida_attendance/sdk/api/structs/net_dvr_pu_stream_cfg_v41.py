from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_dec_stream_mode import NET_DVR_DEC_STREAM_MODE


class struct_tagNET_DVR_PU_STREAM_CFG_V41(Structure):
    pass

_S(struct_tagNET_DVR_PU_STREAM_CFG_V41, [
    ('dwSize', DWORD),
    ('byStreamMode', BYTE),
    ('byStreamEncrypt', BYTE),
    ('byRes1', BYTE * 2),
    ('uDecStreamMode', NET_DVR_DEC_STREAM_MODE),
    ('dwDecDelayTime', DWORD),
    ('sStreamPassword', BYTE * 12),
    ('byRes2', BYTE * 48),
])

NET_DVR_PU_STREAM_CFG_V41 = struct_tagNET_DVR_PU_STREAM_CFG_V41
LPNET_DVR_PU_STREAM_CFG_V41 = POINTER(struct_tagNET_DVR_PU_STREAM_CFG_V41)
tagNET_DVR_PU_STREAM_CFG_V41 = struct_tagNET_DVR_PU_STREAM_CFG_V41
