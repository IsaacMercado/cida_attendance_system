from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLOUDSTORAGE_COND(Structure):
    pass

_S(struct_tagNET_DVR_CLOUDSTORAGE_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes1', BYTE * 64),
])

NET_DVR_CLOUDSTORAGE_COND = struct_tagNET_DVR_CLOUDSTORAGE_COND
LPNET_DVR_CLOUDSTORAGE_COND = POINTER(struct_tagNET_DVR_CLOUDSTORAGE_COND)
tagNET_DVR_CLOUDSTORAGE_COND = struct_tagNET_DVR_CLOUDSTORAGE_COND
