from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_MATRIX_TRUNKPARAM(Structure):
    pass

_S(struct_tagNET_MATRIX_TRUNKPARAM, [
    ('dwSize', DWORD),
    ('dwTrunkId', DWORD),
    ('sTrunkName', BYTE * 32),
    ('dwSrcMonId', DWORD),
    ('dwDstCamId', DWORD),
    ('byTrunkType', BYTE),
    ('byAbility', BYTE),
    ('bySubChan', BYTE),
    ('byLevel', BYTE),
    ('wReserveUserID', WORD),
    ('byRes', BYTE * 18),
])

NET_MATRIX_TRUNKPARAM = struct_tagNET_MATRIX_TRUNKPARAM
LPNET_MATRIX_TRUNKPARAM = POINTER(struct_tagNET_MATRIX_TRUNKPARAM)
tagNET_MATRIX_TRUNKPARAM = struct_tagNET_MATRIX_TRUNKPARAM
