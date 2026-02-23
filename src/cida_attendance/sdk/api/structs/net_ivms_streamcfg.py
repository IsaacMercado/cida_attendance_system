from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_ivms_devsched import NET_IVMS_DEVSCHED


class struct_tagNET_IVMS_STREAMCFG(Structure):
    pass

_S(struct_tagNET_IVMS_STREAMCFG, [
    ('dwSize', DWORD),
    ('struDevSched', (NET_IVMS_DEVSCHED * 4) * 7),
])

NET_IVMS_STREAMCFG = struct_tagNET_IVMS_STREAMCFG
LPNET_IVMS_STREAMCFG = POINTER(struct_tagNET_IVMS_STREAMCFG)
tagNET_IVMS_STREAMCFG = struct_tagNET_IVMS_STREAMCFG
