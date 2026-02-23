from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WINLIST(Structure):
    pass

_S(struct_tagNET_DVR_WINLIST, [
    ('dwSize', DWORD),
    ('wScreenSeq', WORD),
    ('byRes', BYTE * 10),
    ('dwWinNum', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_WINLIST = struct_tagNET_DVR_WINLIST
LPNET_DVR_WINLIST = POINTER(struct_tagNET_DVR_WINLIST)
tagNET_DVR_WINLIST = struct_tagNET_DVR_WINLIST
