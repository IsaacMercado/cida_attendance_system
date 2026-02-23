from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_FAKECARD(Structure):
    pass

_S(struct_tagNET_VCA_FAKECARD, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 7),
])

NET_VCA_FAKECARD = struct_tagNET_VCA_FAKECARD
LPNET_VCA_FAKECARD = POINTER(struct_tagNET_VCA_FAKECARD)
tagNET_VCA_FAKECARD = struct_tagNET_VCA_FAKECARD
