from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_SCANNER(Structure):
    pass

_S(struct_tagNET_VCA_SCANNER, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_SCANNER = struct_tagNET_VCA_SCANNER
LPNET_VCA_SCANNER = POINTER(struct_tagNET_VCA_SCANNER)
tagNET_VCA_SCANNER = struct_tagNET_VCA_SCANNER
