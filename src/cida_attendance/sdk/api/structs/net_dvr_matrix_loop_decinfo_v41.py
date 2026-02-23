from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_matrix_chan_info_v41 import NET_DVR_MATRIX_CHAN_INFO_V41


class struct_tagNET_DVR_MATRIX_LOOP_DECINFO_V41(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_LOOP_DECINFO_V41, [
    ('dwSize', DWORD),
    ('dwPoolTime', DWORD),
    ('struchanConInfo', NET_DVR_MATRIX_CHAN_INFO_V41 * 64),
    ('byStreamEncrypt', BYTE),
    ('byRes', BYTE * 3),
    ('sStreamPassword', BYTE * 12),
])

NET_DVR_MATRIX_LOOP_DECINFO_V41 = struct_tagNET_DVR_MATRIX_LOOP_DECINFO_V41
LPNET_DVR_MATRIX_LOOP_DECINFO_V41 = POINTER(struct_tagNET_DVR_MATRIX_LOOP_DECINFO_V41)
tagNET_DVR_MATRIX_LOOP_DECINFO_V41 = struct_tagNET_DVR_MATRIX_LOOP_DECINFO_V41
