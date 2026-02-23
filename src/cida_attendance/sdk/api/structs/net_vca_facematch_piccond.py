from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_FACEMATCH_PICCOND(Structure):
    pass

_S(struct_tagNET_VCA_FACEMATCH_PICCOND, [
    ('dwSize', DWORD),
    ('dwSnapFaceID', DWORD),
    ('dwBlockListID', DWORD),
    ('dwBlockListFaceID', DWORD),
    ('byRes', BYTE * 20),
])

NET_VCA_FACEMATCH_PICCOND = struct_tagNET_VCA_FACEMATCH_PICCOND
LPNET_VCA_FACEMATCH_PICCOND = POINTER(struct_tagNET_VCA_FACEMATCH_PICCOND)
tagNET_VCA_FACEMATCH_PICCOND = struct_tagNET_VCA_FACEMATCH_PICCOND
