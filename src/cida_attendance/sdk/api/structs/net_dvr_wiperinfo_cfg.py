from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_wipermode_param_union import NET_DVR_WIPERMODE_PARAM_UNION


class struct_tagNET_DVR_WIPERINFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIPERINFO_CFG, [
    ('dwSize', DWORD),
    ('byWiperWorkMode', BYTE),
    ('byRes1', BYTE),
    ('wSensitivity', WORD),
    ('byRes', BYTE * 20),
    ('ustruWiperModeParam', NET_DVR_WIPERMODE_PARAM_UNION),
])

NET_DVR_WIPERINFO_CFG = struct_tagNET_DVR_WIPERINFO_CFG
LPNET_DVR_WIPERINFO_CFG = POINTER(struct_tagNET_DVR_WIPERINFO_CFG)
tagNET_DVR_WIPERINFO_CFG = struct_tagNET_DVR_WIPERINFO_CFG
