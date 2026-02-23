from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DOWNLOAD_CB_INFO(Structure):
    pass

_S(struct_tagNET_DOWNLOAD_CB_INFO, [
    ('dwType', DWORD),
    ('pData', POINTER(BYTE)),
    ('dwDataLen', DWORD),
    ('pFileInfo', POINTER(None)),
    ('dwFileInfoLen', DWORD),
    ('byRes', BYTE * 120),
])

NET_DOWNLOAD_CB_INFO = struct_tagNET_DOWNLOAD_CB_INFO
LPNET_DOWNLOAD_CB_INFO = POINTER(struct_tagNET_DOWNLOAD_CB_INFO)
tagNET_DOWNLOAD_CB_INFO = struct_tagNET_DOWNLOAD_CB_INFO
