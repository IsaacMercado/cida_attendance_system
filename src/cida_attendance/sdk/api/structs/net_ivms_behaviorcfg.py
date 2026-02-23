from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_ivms_rulecfg import NET_IVMS_RULECFG


class struct_tagNET_IVMS_BEHAVIORCFG(Structure):
    pass

_S(struct_tagNET_IVMS_BEHAVIORCFG, [
    ('dwSize', DWORD),
    ('byPicProType', BYTE),
    ('byRes', BYTE * 3),
    ('struPicParam', NET_DVR_JPEGPARA),
    ('struRuleCfg', (NET_IVMS_RULECFG * 4) * 7),
])

NET_IVMS_BEHAVIORCFG = struct_tagNET_IVMS_BEHAVIORCFG
LPNET_IVMS_BEHAVIORCFG = POINTER(struct_tagNET_IVMS_BEHAVIORCFG)
tagNET_IVMS_BEHAVIORCFG = struct_tagNET_IVMS_BEHAVIORCFG
