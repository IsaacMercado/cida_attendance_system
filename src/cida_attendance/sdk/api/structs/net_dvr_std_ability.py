from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STD_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_STD_ABILITY, [
    ('lpCondBuffer', POINTER(None)),
    ('dwCondSize', DWORD),
    ('lpOutBuffer', POINTER(None)),
    ('dwOutSize', DWORD),
    ('lpStatusBuffer', POINTER(None)),
    ('dwStatusSize', DWORD),
    ('dwRetSize', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_STD_ABILITY = struct_tagNET_DVR_STD_ABILITY
LPNET_DVR_STD_ABILITY = POINTER(struct_tagNET_DVR_STD_ABILITY)
tagNET_DVR_STD_ABILITY = struct_tagNET_DVR_STD_ABILITY
