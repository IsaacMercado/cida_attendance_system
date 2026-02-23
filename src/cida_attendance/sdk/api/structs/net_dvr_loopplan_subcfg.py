from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_176 import NET_DVR_MATRIX_CHAN_INFO_V30


class struct_tagNET_DVR_LOOPPLAN_SUBCFG(Structure):
    pass

_S(struct_tagNET_DVR_LOOPPLAN_SUBCFG, [
    ('dwSize', DWORD),
    ('dwPoolTime', DWORD),
    ('struChanConInfo', NET_DVR_MATRIX_CHAN_INFO_V30 * 64),
    ('byRes', BYTE * 16),
])

NET_DVR_LOOPPLAN_SUBCFG = struct_tagNET_DVR_LOOPPLAN_SUBCFG
LPNET_DVR_LOOPPLAN_SUBCFG = POINTER(struct_tagNET_DVR_LOOPPLAN_SUBCFG)
tagNET_DVR_LOOPPLAN_SUBCFG = struct_tagNET_DVR_LOOPPLAN_SUBCFG
