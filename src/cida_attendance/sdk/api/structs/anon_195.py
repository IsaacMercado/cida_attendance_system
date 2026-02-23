from ctypes import Structure

from ..base_classes import _S, BYTE, HWND, LONG
from ..ctypes_preamble import POINTER, String


class struct_anon_195(Structure):
    pass

_S(struct_anon_195, [
    ('lChannel', LONG),
    ('lLinkMode', LONG),
    ('hPlayWnd', HWND),
    ('sMultiCastIP', String),
    ('byProtoType', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_CLIENTINFO = struct_anon_195
LPNET_DVR_CLIENTINFO = POINTER(struct_anon_195)
