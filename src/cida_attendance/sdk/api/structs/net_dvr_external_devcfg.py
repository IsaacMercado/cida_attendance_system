from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_428 import union_anon_428


class struct_tagNET_DVR_EXTERNAL_DEVCFG(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_DEVCFG, [
    ('dwSize', DWORD),
    ('byExternalDevTpye', BYTE),
    ('byRes2', BYTE * 3),
    ('sDevName', c_char * 32),
    ('uExternalDevInfo', union_anon_428),
    ('byRes', BYTE * 128),
])

NET_DVR_EXTERNAL_DEVCFG = struct_tagNET_DVR_EXTERNAL_DEVCFG
LPNET_DVR_EXTERNAL_DEVCFG = POINTER(struct_tagNET_DVR_EXTERNAL_DEVCFG)
tagNET_DVR_EXTERNAL_DEVCFG = struct_tagNET_DVR_EXTERNAL_DEVCFG
