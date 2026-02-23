from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_outputparam import NET_DVR_OUTPUTPARAM


class struct_tagNET_DVR_OUTPUTCFG(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUTCFG, [
    ('dwSize', DWORD),
    ('byScreenLayX', BYTE),
    ('byScreenLayY', BYTE),
    ('wOutputChanNum', WORD),
    ('byRes1', BYTE * 4),
    ('struOutputParam', NET_DVR_OUTPUTPARAM),
    ('sWallName', BYTE * 16),
    ('byRes2', BYTE * 8),
])

NET_DVR_OUTPUTCFG = struct_tagNET_DVR_OUTPUTCFG
LPNET_DVR_OUTPUTCFG = POINTER(struct_tagNET_DVR_OUTPUTCFG)
tagNET_DVR_OUTPUTCFG = struct_tagNET_DVR_OUTPUTCFG
