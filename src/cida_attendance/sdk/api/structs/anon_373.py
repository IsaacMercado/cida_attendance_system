from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_372 import union_anon_372


class struct_anon_373(Structure):
    pass

_S(struct_anon_373, [
    ('dwSize', DWORD),
    ('byEnableFTP', BYTE),
    ('byProtocolType', BYTE),
    ('wFTPPort', WORD),
    ('unionServer', union_anon_372),
    ('szUserName', BYTE * 32),
    ('szPassWORD', BYTE * 16),
    ('szTopCustomDir', BYTE * 64),
    ('szSubCustomDir', BYTE * 64),
    ('byDirLevel', BYTE),
    ('byTopDirMode', BYTE),
    ('bySubDirMode', BYTE),
    ('byType', BYTE),
    ('byEnableAnony', BYTE),
    ('byAddresType', BYTE),
    ('byRes2', BYTE * 198),
])

NET_DVR_FTP_SERVER_TEST_PARA = struct_anon_373
LPNET_DVR_FTP_SERVER_TEST_PARA = POINTER(struct_anon_373)
