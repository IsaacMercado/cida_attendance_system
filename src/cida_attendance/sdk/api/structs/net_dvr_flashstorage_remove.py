from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FLASHSTORAGE_REMOVE(Structure):
    pass

_S(struct_tagNET_DVR_FLASHSTORAGE_REMOVE, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byPDCRemoveEnable', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_FLASHSTORAGE_REMOVE = struct_tagNET_DVR_FLASHSTORAGE_REMOVE
LPNET_DVR_FLASHSTORAGE_REMOVE = POINTER(struct_tagNET_DVR_FLASHSTORAGE_REMOVE)
tagNET_DVR_FLASHSTORAGE_REMOVE = struct_tagNET_DVR_FLASHSTORAGE_REMOVE
