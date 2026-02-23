from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_CHAN_IN_PARAM(Structure):
    pass

_S(struct_tagNET_VCA_CHAN_IN_PARAM, [
    ('byVCAType', BYTE),
    ('byMode', BYTE),
    ('byRes', BYTE * 2),
])

NET_VCA_CHAN_IN_PARAM = struct_tagNET_VCA_CHAN_IN_PARAM
LPNET_VCA_CHAN_IN_PARAM = POINTER(struct_tagNET_VCA_CHAN_IN_PARAM)
tagNET_VCA_CHAN_IN_PARAM = struct_tagNET_VCA_CHAN_IN_PARAM
