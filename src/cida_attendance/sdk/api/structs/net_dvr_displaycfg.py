from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_displayparam import NET_DVR_DISPLAYPARAM


class struct_tagNET_DVR_DISPLAYCFG(Structure):
    pass

_S(struct_tagNET_DVR_DISPLAYCFG, [
    ('dwSize', DWORD),
    ('struDisplayParam', NET_DVR_DISPLAYPARAM * 512),
    ('byRes', BYTE * 128),
])

NET_DVR_DISPLAYCFG = struct_tagNET_DVR_DISPLAYCFG
LPNET_DVR_DISPLAYCFG = POINTER(struct_tagNET_DVR_DISPLAYCFG)
tagNET_DVR_DISPLAYCFG = struct_tagNET_DVR_DISPLAYCFG
