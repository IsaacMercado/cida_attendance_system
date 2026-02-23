from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_FIND_MATCHPIC_RESULT(Structure):
    pass

_S(struct_tagNET_VCA_FIND_MATCHPIC_RESULT, [
    ('dwSize', DWORD),
    ('dwDataBaseType', DWORD),
    ('dwDataBaseID', DWORD),
    ('dwRecordID', DWORD),
    ('dwPicLen', DWORD),
    ('byRes', BYTE * 64),
    ('pPicBuffer', POINTER(BYTE)),
])

NET_VCA_FIND_MATCHPIC_RESULT = struct_tagNET_VCA_FIND_MATCHPIC_RESULT
LPNET_VCA_FIND_MATCHPIC_RESULT = POINTER(struct_tagNET_VCA_FIND_MATCHPIC_RESULT)
tagNET_VCA_FIND_MATCHPIC_RESULT = struct_tagNET_VCA_FIND_MATCHPIC_RESULT
