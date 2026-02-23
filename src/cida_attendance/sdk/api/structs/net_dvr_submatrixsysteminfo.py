from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_NET_DVR_SUBMATRIXSYSTEMINFO(Structure):
    pass

_S(struct_NET_DVR_SUBMATRIXSYSTEMINFO, [
    ('dwSequence', DWORD),
    ('sAddress', BYTE * 64),
    ('wSubMatrixPort', WORD),
    ('byRes1', BYTE * 6),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byRes2', BYTE * 36),
])

NET_DVR_SUBMATRIXSYSTEMINFO = struct_NET_DVR_SUBMATRIXSYSTEMINFO
LPNET_DVR_SUBMATRIXSYSTEMINFO = POINTER(struct_NET_DVR_SUBMATRIXSYSTEMINFO)
NET_DVR_SUBMATRIXSYSTEMINFO = struct_NET_DVR_SUBMATRIXSYSTEMINFO
