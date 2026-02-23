from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BUF_INFO(Structure):
    pass

_S(struct_tagNET_DVR_BUF_INFO, [
    ('pBuf', POINTER(None)),
    ('nLen', DWORD),
])

NET_DVR_BUF_INFO = struct_tagNET_DVR_BUF_INFO
LPNET_DVR_BUF_INFO = POINTER(struct_tagNET_DVR_BUF_INFO)
tagNET_DVR_BUF_INFO = struct_tagNET_DVR_BUF_INFO
