from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40


class struct_tagNET_VCA_DEFOCUSPARAM(Structure):
    pass

_S(struct_tagNET_VCA_DEFOCUSPARAM, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySensitiveLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('byRes2', BYTE * 24),
])

NET_VCA_DEFOCUSPARAM = struct_tagNET_VCA_DEFOCUSPARAM
LPNET_VCA_DEFOCUSPARAM = POINTER(struct_tagNET_VCA_DEFOCUSPARAM)
tagNET_VCA_DEFOCUSPARAM = struct_tagNET_VCA_DEFOCUSPARAM
