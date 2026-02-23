from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_MATRIX_RESOURSEGROUPPARAM(Structure):
    pass

_S(struct_tagNET_MATRIX_RESOURSEGROUPPARAM, [
    ('dwSize', DWORD),
    ('byGroupName', BYTE * 32),
    ('byGroupType', BYTE),
    ('byRes1', BYTE),
    ('wMemNum', WORD),
    ('dwGlobalId', DWORD * 512),
    ('byRes2', BYTE * 20),
])

NET_MATRIX_RESOURCEGROUPPARAM = struct_tagNET_MATRIX_RESOURSEGROUPPARAM
LPNET_MATRIX_RESOURSEGROUPPARAM = POINTER(struct_tagNET_MATRIX_RESOURSEGROUPPARAM)
tagNET_MATRIX_RESOURSEGROUPPARAM = struct_tagNET_MATRIX_RESOURSEGROUPPARAM
