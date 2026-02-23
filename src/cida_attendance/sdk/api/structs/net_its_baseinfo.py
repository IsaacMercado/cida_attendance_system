from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_BASEINFO(Structure):
    pass

_S(struct_tagNET_ITS_BASEINFO, [
    ('dwSize', DWORD),
    ('byMainVer', BYTE * 32),
    ('byMprVer', BYTE * 32),
    ('byBvtVer', BYTE * 32),
    ('byLptVer', BYTE * 32),
    ('byTvdVer', BYTE * 32),
    ('byTldVer', BYTE * 32),
    ('byRes', BYTE * 252),
])

NET_ITS_BASEINFO = struct_tagNET_ITS_BASEINFO
LPNET_ITS_BASEINFO = POINTER(struct_tagNET_ITS_BASEINFO)
tagNET_ITS_BASEINFO = struct_tagNET_ITS_BASEINFO
