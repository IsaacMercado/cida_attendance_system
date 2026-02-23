from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_CTRLINFO(Structure):
    pass

_S(struct_tagNET_VCA_CTRLINFO, [
    ('byVCAEnable', BYTE),
    ('byVCAType', BYTE),
    ('byStreamWithVCA', BYTE),
    ('byMode', BYTE),
    ('byControlType', BYTE),
    ('byPicWithVCA', BYTE),
    ('byRes', BYTE * 2),
])

NET_VCA_CTRLINFO = struct_tagNET_VCA_CTRLINFO
LPNET_VCA_CTRLINFO = POINTER(struct_tagNET_VCA_CTRLINFO)
tagNET_VCA_CTRLINFO = struct_tagNET_VCA_CTRLINFO
