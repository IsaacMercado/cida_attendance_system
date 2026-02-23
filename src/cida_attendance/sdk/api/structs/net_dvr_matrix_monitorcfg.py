from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_disp_chan_info import NET_DVR_DISP_CHAN_INFO


class struct_tagNET_DVR_MATRIX_MONITORCFG(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_MONITORCFG, [
    ('dwGlobalIndex', DWORD),
    ('dwInterIndex', DWORD),
    ('sMonName', BYTE * 32),
    ('struDispChanCfg', NET_DVR_DISP_CHAN_INFO),
])

NET_DVR_MATRIX_MONITORCFG = struct_tagNET_DVR_MATRIX_MONITORCFG
LPNET_DVR_MATRIX_MONITORCFG = POINTER(struct_tagNET_DVR_MATRIX_MONITORCFG)
tagNET_DVR_MATRIX_MONITORCFG = struct_tagNET_DVR_MATRIX_MONITORCFG
