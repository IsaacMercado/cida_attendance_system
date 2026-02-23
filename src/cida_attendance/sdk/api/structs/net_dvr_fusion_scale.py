from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FUSION_SCALE(Structure):
    pass

_S(struct_tagNET_DVR_FUSION_SCALE, [
    ('dwSize', DWORD),
    ('wWidth', WORD),
    ('wHeight', WORD),
    ('byRes', BYTE * 32),
])

NET_DVR_FUSION_SCALE = struct_tagNET_DVR_FUSION_SCALE
LPNET_DVR_FUSION_SCALE = POINTER(struct_tagNET_DVR_FUSION_SCALE)
tagNET_DVR_FUSION_SCALE = struct_tagNET_DVR_FUSION_SCALE
