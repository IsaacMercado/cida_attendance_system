from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RES_INFO(Structure):
    pass

_S(struct_tagNET_DVR_RES_INFO, [
    ('dwImageWidth', DWORD),
    ('dwImageHeight', DWORD),
])

NET_DVR_RES_INFO = struct_tagNET_DVR_RES_INFO
LPNET_DVR_RES_INFO = POINTER(struct_tagNET_DVR_RES_INFO)
tagNET_DVR_RES_INFO = struct_tagNET_DVR_RES_INFO
