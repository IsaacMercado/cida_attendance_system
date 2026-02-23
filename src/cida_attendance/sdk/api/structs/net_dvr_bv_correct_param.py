from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_binoc_rectify_param import NET_DVR_BINOC_RECTIFY_PARAM


class struct__tagNET_DVR_BV_CORRECT_PARAM(Structure):
    pass

_S(struct__tagNET_DVR_BV_CORRECT_PARAM, [
    ('dwSize', DWORD),
    ('fReprojectMatrix', (c_float * 4) * 4),
    ('struLCamParam', NET_DVR_BINOC_RECTIFY_PARAM),
    ('struRCamParam', NET_DVR_BINOC_RECTIFY_PARAM),
    ('byLensType', BYTE),
    ('byRes1', BYTE * 3),
    ('fRotateMatrix', (c_float * 3) * 3),
    ('fTransMatrix', c_float * 3),
    ('dwOriImgWidth', DWORD),
    ('dwOriImgHeight', DWORD),
    ('byRes', BYTE * 196),
])

NET_DVR_BV_CORRECT_PARAM = struct__tagNET_DVR_BV_CORRECT_PARAM
LPNET_DVR_BV_CORRECT_PARAM = POINTER(struct__tagNET_DVR_BV_CORRECT_PARAM)
_tagNET_DVR_BV_CORRECT_PARAM = struct__tagNET_DVR_BV_CORRECT_PARAM
