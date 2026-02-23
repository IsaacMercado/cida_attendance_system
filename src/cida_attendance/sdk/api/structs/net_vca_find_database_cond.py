from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_FIND_DATABASE_COND(Structure):
    pass

_S(struct_tagNET_VCA_FIND_DATABASE_COND, [
    ('dwDataBaseType', DWORD),
    ('byRes', BYTE * 12),
])

NET_VCA_FIND_DATABASE_COND = struct_tagNET_VCA_FIND_DATABASE_COND
LPNET_VCA_FIND_DATABASE_COND = POINTER(struct_tagNET_VCA_FIND_DATABASE_COND)
tagNET_VCA_FIND_DATABASE_COND = struct_tagNET_VCA_FIND_DATABASE_COND
