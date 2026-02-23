from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_MATRIX_USERPARAM(Structure):
    pass

_S(struct_tagNET_MATRIX_USERPARAM, [
    ('dwSize', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byRole', BYTE),
    ('byLevel', BYTE),
    ('byRes', BYTE * 18),
])

NET_MATRIX_USERPARAM = struct_tagNET_MATRIX_USERPARAM
LPNET_MATRIX_USERPARAM = POINTER(struct_tagNET_MATRIX_USERPARAM)
tagNET_MATRIX_USERPARAM = struct_tagNET_MATRIX_USERPARAM
