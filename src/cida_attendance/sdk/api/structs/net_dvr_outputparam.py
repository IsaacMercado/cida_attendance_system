from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_videoeffect import NET_DVR_VIDEOEFFECT


class struct_tagNET_DVR_OUTPUTPARAM(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUTPARAM, [
    ('dwSize', DWORD),
    ('byMonMode', BYTE),
    ('byRes1', BYTE * 3),
    ('dwResolution', DWORD),
    ('struVideoEffect', NET_DVR_VIDEOEFFECT),
    ('byRes2', BYTE * 32),
])

NET_DVR_OUTPUTPARAM = struct_tagNET_DVR_OUTPUTPARAM
LPNET_DVR_OUTPUTPARAM = POINTER(struct_tagNET_DVR_OUTPUTPARAM)
tagNET_DVR_OUTPUTPARAM = struct_tagNET_DVR_OUTPUTPARAM
