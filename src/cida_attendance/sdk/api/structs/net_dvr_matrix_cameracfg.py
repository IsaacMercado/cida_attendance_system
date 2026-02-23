from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_matrix_pu_stream_cfg import NET_MATRIX_PU_STREAM_CFG


class struct_tagNET_DVR_MATRIX_CAMERACFG(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_CAMERACFG, [
    ('dwGlobalIndex', DWORD),
    ('dwInterIndex', DWORD),
    ('sCamName', BYTE * 32),
    ('struPuStreamCfg', NET_MATRIX_PU_STREAM_CFG),
])

NET_DVR_MATRIX_CAMERACFG = struct_tagNET_DVR_MATRIX_CAMERACFG
LPNET_DVR_MATRIX_CAMERACFG = POINTER(struct_tagNET_DVR_MATRIX_CAMERACFG)
tagNET_DVR_MATRIX_CAMERACFG = struct_tagNET_DVR_MATRIX_CAMERACFG
