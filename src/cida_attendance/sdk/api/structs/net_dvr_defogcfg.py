from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEFOGCFG(Structure):
    pass

_S(struct_tagNET_DVR_DEFOGCFG, [
    ('byMode', BYTE),
    ('byLevel', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_DEFOGCFG = struct_tagNET_DVR_DEFOGCFG
LPNET_DVR_DEFOGCFG = POINTER(struct_tagNET_DVR_DEFOGCFG)
tagNET_DVR_DEFOGCFG = struct_tagNET_DVR_DEFOGCFG
