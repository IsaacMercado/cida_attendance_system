from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_DATABASE_PARAM(Structure):
    pass

_S(struct_tagNET_VCA_DATABASE_PARAM, [
    ('dwSize', DWORD),
    ('dwDataBaseID', DWORD),
    ('dwDataBaseType', DWORD),
    ('byDataBaseName', BYTE * 32),
    ('byAttribute', BYTE * 64),
    ('byRes', BYTE * 20),
])

NET_VCA_DATABASE_PARAM = struct_tagNET_VCA_DATABASE_PARAM
LPNET_VCA_DATABASE_PARAM = POINTER(struct_tagNET_VCA_DATABASE_PARAM)
tagNET_VCA_DATABASE_PARAM = struct_tagNET_VCA_DATABASE_PARAM
