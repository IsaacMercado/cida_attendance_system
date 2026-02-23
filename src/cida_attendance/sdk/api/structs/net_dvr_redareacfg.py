from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_correct_params import NET_DVR_CORRECT_PARAMS
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_REDAREACFG(Structure):
    pass

_S(struct_tagNET_DVR_REDAREACFG, [
    ('dwSize', DWORD),
    ('dwCorrectEnable', DWORD),
    ('dwCorrectLevel', DWORD),
    ('dwAreaNum', DWORD),
    ('struLaneRect', NET_VCA_RECT * 6),
    ('struCorrectParam', NET_DVR_CORRECT_PARAMS * 6),
    ('byRes2', BYTE * 8),
])

NET_DVR_REDAREACFG = struct_tagNET_DVR_REDAREACFG
LPNET_DVR_REDAREACFG = POINTER(struct_tagNET_DVR_REDAREACFG)
tagNET_DVR_REDAREACFG = struct_tagNET_DVR_REDAREACFG
