from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_296(Structure):
    pass

_S(struct_anon_296, [
    ('dwSize', DWORD),
    ('dwEnableFTP', DWORD),
    ('sFTPIP', c_char * 16),
    ('dwFTPPort', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwDirLevel', DWORD),
    ('wTopDirMode', WORD),
    ('wSubDirMode', WORD),
    ('byEnableAnony', BYTE),
    ('byPicArchivingInterval', BYTE),
    ('byRes', BYTE * 22),
])

NET_DVR_FTPCFG = struct_anon_296
LPNET_DVR_FTPCFG = POINTER(struct_anon_296)
