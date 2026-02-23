from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEVLIST(Structure):
    pass

_S(struct_tagNET_DVR_DEVLIST, [
    ('dwSize', DWORD),
    ('dwDevNums', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('byRes1', BYTE * 3),
    ('dwBufLen', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_DEVLIST = struct_tagNET_DVR_DEVLIST
LPNET_DVR_DEVLIST = POINTER(struct_tagNET_DVR_DEVLIST)
tagNET_DVR_DEVLIST = struct_tagNET_DVR_DEVLIST
