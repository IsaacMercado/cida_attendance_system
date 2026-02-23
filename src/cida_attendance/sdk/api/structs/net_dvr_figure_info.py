from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_FIGURE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FIGURE_INFO, [
    ('dwPicLen', DWORD),
    ('pPicBuf', String),
])

NET_DVR_FIGURE_INFO = struct_tagNET_DVR_FIGURE_INFO
LPNET_DVR_FIGURE_INFO = POINTER(struct_tagNET_DVR_FIGURE_INFO)
tagNET_DVR_FIGURE_INFO = struct_tagNET_DVR_FIGURE_INFO
