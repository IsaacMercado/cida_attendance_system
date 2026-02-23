from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHAN_RELATION_RESOURCE(Structure):
    pass

_S(struct_tagNET_DVR_CHAN_RELATION_RESOURCE, [
    ('dwSize', DWORD),
    ('dwDisplayChan', DWORD),
    ('byRelateAudio', BYTE),
    ('byRes1', BYTE * 3),
    ('dwSubWinNo', DWORD),
    ('dwChannel', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_CHAN_RELATION_RESOURCE = struct_tagNET_DVR_CHAN_RELATION_RESOURCE
LPNET_DVR_CHAN_RELATION_RESOURCE = POINTER(struct_tagNET_DVR_CHAN_RELATION_RESOURCE)
tagNET_DVR_CHAN_RELATION_RESOURCE = struct_tagNET_DVR_CHAN_RELATION_RESOURCE
