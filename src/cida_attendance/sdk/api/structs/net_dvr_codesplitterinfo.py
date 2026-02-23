from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_CODESPLITTERINFO(Structure):
    pass

_S(struct_tagNET_DVR_CODESPLITTERINFO, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes1', BYTE * 6),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byChan', BYTE),
    ('by485Port', BYTE),
    ('byRes2', BYTE * 14),
])

NET_DVR_CODESPLITTERINFO = struct_tagNET_DVR_CODESPLITTERINFO
LPNET_DVR_CODESPLITTERINFO = POINTER(struct_tagNET_DVR_CODESPLITTERINFO)
tagNET_DVR_CODESPLITTERINFO = struct_tagNET_DVR_CODESPLITTERINFO
