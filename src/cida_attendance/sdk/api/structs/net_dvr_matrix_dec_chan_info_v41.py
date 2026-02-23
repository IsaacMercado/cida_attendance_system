from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_dec_stream_mode import NET_DVR_DEC_STREAM_MODE
from .net_matrix_passivemode import NET_DVR_MATRIX_PASSIVEMODE


class struct_tagNET_DVR_MATRIX_DEC_CHAN_INFO_V41(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_DEC_CHAN_INFO_V41, [
    ('dwSize', DWORD),
    ('byStreamMode', BYTE),
    ('byRes1', BYTE * 3),
    ('uDecStreamMode', NET_DVR_DEC_STREAM_MODE),
    ('dwPlayMode', DWORD),
    ('StartTime', NET_DVR_TIME),
    ('StopTime', NET_DVR_TIME),
    ('sFileName', c_char * 128),
    ('dwGetStreamMode', DWORD),
    ('struPassiveMode', NET_DVR_MATRIX_PASSIVEMODE),
    ('byRes2', BYTE * 32),
])

NET_DVR_MATRIX_DEC_CHAN_INFO_V41 = struct_tagNET_DVR_MATRIX_DEC_CHAN_INFO_V41
LPNET_DVR_MATRIX_DEC_CHAN_INFO_V41 = POINTER(struct_tagNET_DVR_MATRIX_DEC_CHAN_INFO_V41)
tagNET_DVR_MATRIX_DEC_CHAN_INFO_V41 = struct_tagNET_DVR_MATRIX_DEC_CHAN_INFO_V41
