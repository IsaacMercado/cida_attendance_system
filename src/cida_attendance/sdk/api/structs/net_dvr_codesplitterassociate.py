from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_CODESPLITTERASSOCIATE(Structure):
    pass

_S(struct_tagNET_DVR_CODESPLITTERASSOCIATE, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes1', BYTE * 6),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byChan', BYTE),
    ('byRes2', BYTE * 15),
])

NET_DVR_CODESPLITTERASSOCIATE = struct_tagNET_DVR_CODESPLITTERASSOCIATE
LPNET_DVR_CODESPLITTERASSOCIATE = POINTER(struct_tagNET_DVR_CODESPLITTERASSOCIATE)
tagNET_DVR_CODESPLITTERASSOCIATE = struct_tagNET_DVR_CODESPLITTERASSOCIATE
