from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_FACEMATCH_PICTURE(Structure):
    pass

_S(struct_tagNET_VCA_FACEMATCH_PICTURE, [
    ('dwSize', DWORD),
    ('dwSnapFaceLen', DWORD),
    ('dwBlockListFaceLen', DWORD),
    ('byRes', BYTE * 20),
    ('pSnapFace', POINTER(BYTE)),
    ('pBlockListFace', POINTER(BYTE)),
])

NET_VCA_FACEMATCH_PICTURE = struct_tagNET_VCA_FACEMATCH_PICTURE
LPNET_VCA_FACEMATCH_PICTURE = POINTER(struct_tagNET_VCA_FACEMATCH_PICTURE)
tagNET_VCA_FACEMATCH_PICTURE = struct_tagNET_VCA_FACEMATCH_PICTURE
