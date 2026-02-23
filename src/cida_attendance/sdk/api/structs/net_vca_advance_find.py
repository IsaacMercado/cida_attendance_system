from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_ADVANCE_FIND(Structure):
    pass

_S(struct_tagNET_VCA_ADVANCE_FIND, [
    ('dwFacePicID', DWORD),
    ('byRes', BYTE * 36),
])

NET_VCA_ADVANCE_FIND = struct_tagNET_VCA_ADVANCE_FIND
LPNET_VCA_ADVANCE_FIND = POINTER(struct_tagNET_VCA_ADVANCE_FIND)
tagNET_VCA_ADVANCE_FIND = struct_tagNET_VCA_ADVANCE_FIND
