from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_HUMAN_ENTER(Structure):
    pass

_S(struct_tagNET_VCA_HUMAN_ENTER, [
    ('dwRes', DWORD * 23),
])

NET_VCA_HUMAN_ENTER = struct_tagNET_VCA_HUMAN_ENTER
LPNET_VCA_HUMAN_ENTER = POINTER(struct_tagNET_VCA_HUMAN_ENTER)
tagNET_VCA_HUMAN_ENTER = struct_tagNET_VCA_HUMAN_ENTER
