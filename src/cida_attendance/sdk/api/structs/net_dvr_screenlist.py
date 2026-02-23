from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREENLIST(Structure):
    pass

_S(struct_tagNET_DVR_SCREENLIST, [
    ('dwSize', DWORD),
    ('byWallNo', BYTE),
    ('byRes', BYTE * 11),
    ('dwScreenNums', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_SCREENLIST = struct_tagNET_DVR_SCREENLIST
LPNET_DVR_SCREENLIST = POINTER(struct_tagNET_DVR_SCREENLIST)
tagNET_DVR_SCREENLIST = struct_tagNET_DVR_SCREENLIST
