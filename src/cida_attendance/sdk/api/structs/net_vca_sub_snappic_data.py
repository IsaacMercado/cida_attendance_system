from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_VCA_SUB_SNAPPIC_DATA(Structure):
    pass

_S(struct_tagNET_VCA_SUB_SNAPPIC_DATA, [
    ('dwFacePicID', DWORD),
    ('dwFacePicLen', DWORD),
    ('struSnapTime', NET_DVR_TIME),
    ('dwSimilarity', DWORD),
    ('byRes', BYTE * 16),
    ('sPicBuf', c_char * 6144),
])

NET_VCA_SUB_SNAPPIC_DATA = struct_tagNET_VCA_SUB_SNAPPIC_DATA
LPNET_VCA_SUB_SNAPPIC_DATA = POINTER(struct_tagNET_VCA_SUB_SNAPPIC_DATA)
tagNET_VCA_SUB_SNAPPIC_DATA = struct_tagNET_VCA_SUB_SNAPPIC_DATA
