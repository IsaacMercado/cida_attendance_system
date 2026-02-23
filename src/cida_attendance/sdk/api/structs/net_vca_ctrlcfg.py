from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_ctrlinfo import NET_VCA_CTRLINFO


class struct_tagNET_VCA_CTRLCFG(Structure):
    pass

_S(struct_tagNET_VCA_CTRLCFG, [
    ('dwSize', DWORD),
    ('struCtrlInfo', NET_VCA_CTRLINFO * 16),
    ('byRes', BYTE * 16),
])

NET_VCA_CTRLCFG = struct_tagNET_VCA_CTRLCFG
LPNET_VCA_CTRLCFG = POINTER(struct_tagNET_VCA_CTRLCFG)
tagNET_VCA_CTRLCFG = struct_tagNET_VCA_CTRLCFG
