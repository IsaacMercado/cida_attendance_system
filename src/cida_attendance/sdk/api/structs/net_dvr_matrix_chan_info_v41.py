from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_dec_stream_mode import NET_DVR_DEC_STREAM_MODE


class struct_tagNET_DVR_MATRIX_CHAN_INFO_V41(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_CHAN_INFO_V41, [
    ('byEnable', BYTE),
    ('byStreamMode', BYTE),
    ('byRes', BYTE * 2),
    ('uDecStreamMode', NET_DVR_DEC_STREAM_MODE),
])

NET_DVR_MATRIX_CHAN_INFO_V41 = struct_tagNET_DVR_MATRIX_CHAN_INFO_V41
LPNET_DVR_MATRIX_CHAN_INFO_V41 = POINTER(struct_tagNET_DVR_MATRIX_CHAN_INFO_V41)
tagNET_DVR_MATRIX_CHAN_INFO_V41 = struct_tagNET_DVR_MATRIX_CHAN_INFO_V41
