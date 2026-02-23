from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_matrix_tran_chan_info_v30 import NET_DVR_MATRIX_TRAN_CHAN_INFO_V30


class struct_tagMATRIX_TRAN_CHAN_CONFIG(Structure):
    pass

_S(struct_tagMATRIX_TRAN_CHAN_CONFIG, [
    ('dwSize', DWORD),
    ('by232IsDualChan', BYTE),
    ('by485IsDualChan', BYTE),
    ('vyRes', BYTE * 2),
    ('struTranInfo', NET_DVR_MATRIX_TRAN_CHAN_INFO_V30 * 64),
])

NET_DVR_MATRIX_TRAN_CHAN_CONFIG_V30 = struct_tagMATRIX_TRAN_CHAN_CONFIG
LPNET_DVR_MATRIX_TRAN_CHAN_CONFIG_V30 = POINTER(struct_tagMATRIX_TRAN_CHAN_CONFIG)
tagMATRIX_TRAN_CHAN_CONFIG = struct_tagMATRIX_TRAN_CHAN_CONFIG
