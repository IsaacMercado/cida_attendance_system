from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PREVIEW_DISPLAYCFG(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEW_DISPLAYCFG, [
    ('dwSize', DWORD),
    ('byCorrectMode', BYTE),
    ('byMountType', BYTE),
    ('byRealTimeOutput', BYTE),
    ('byRes', BYTE * 61),
])

NET_DVR_PREVIEW_DISPLAYCFG = struct_tagNET_DVR_PREVIEW_DISPLAYCFG
LPNET_DVR_PREVIEW_DISPLAYCFG = POINTER(struct_tagNET_DVR_PREVIEW_DISPLAYCFG)
tagNET_DVR_PREVIEW_DISPLAYCFG = struct_tagNET_DVR_PREVIEW_DISPLAYCFG
