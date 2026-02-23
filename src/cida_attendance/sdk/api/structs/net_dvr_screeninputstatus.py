from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREENINPUTSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_SCREENINPUTSTATUS, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 12),
    ('dwNums', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_SCREENINPUTSTATUS = struct_tagNET_DVR_SCREENINPUTSTATUS
LPNET_DVR_SCREENINPUTSTATUS = POINTER(struct_tagNET_DVR_SCREENINPUTSTATUS)
tagNET_DVR_SCREENINPUTSTATUS = struct_tagNET_DVR_SCREENINPUTSTATUS
