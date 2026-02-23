from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_DELETE_DATABASE_COND(Structure):
    pass

_S(struct_tagNET_VCA_DELETE_DATABASE_COND, [
    ('dwSize', DWORD),
    ('dwDataBaseType', DWORD),
    ('dwDataBaseID', DWORD),
    ('byRes', BYTE * 64),
])

NET_VCA_DELETE_DATABASE_COND = struct_tagNET_VCA_DELETE_DATABASE_COND
LPNET_VCA_DELETE_DATABASE_COND = POINTER(struct_tagNET_VCA_DELETE_DATABASE_COND)
tagNET_VCA_DELETE_DATABASE_COND = struct_tagNET_VCA_DELETE_DATABASE_COND
