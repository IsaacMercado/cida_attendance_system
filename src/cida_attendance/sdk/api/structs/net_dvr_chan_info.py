from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_26 import NET_DVR_COLOR


class struct_tagNET_DVR_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CHAN_INFO, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('sChanName', BYTE * 32),
    ('struVideoColor', NET_DVR_COLOR),
    ('wResolutionX', WORD),
    ('wResolutionY', WORD),
    ('byRes2', BYTE * 40),
])

NET_DVR_CHAN_INFO = struct_tagNET_DVR_CHAN_INFO
LPNET_DVR_CHAN_INFO = POINTER(struct_tagNET_DVR_CHAN_INFO)
tagNET_DVR_CHAN_INFO = struct_tagNET_DVR_CHAN_INFO
