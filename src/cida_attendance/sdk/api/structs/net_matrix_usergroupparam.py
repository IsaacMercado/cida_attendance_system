from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_MATRIX_USERGROUPPARAM(Structure):
    pass

_S(struct_tagNET_MATRIX_USERGROUPPARAM, [
    ('dwSize', DWORD),
    ('sGroupName', BYTE * 32),
    ('wUserMember', WORD * 255),
    ('wResorceGroupMember', WORD * 255),
    ('byPermission', BYTE * 32),
    ('byRes', BYTE * 20),
])

NET_MATRIX_USERGROUPPARAM = struct_tagNET_MATRIX_USERGROUPPARAM
LPNET_MATRIX_USERGROUPPARAM = POINTER(struct_tagNET_MATRIX_USERGROUPPARAM)
tagNET_MATRIX_USERGROUPPARAM = struct_tagNET_MATRIX_USERGROUPPARAM
