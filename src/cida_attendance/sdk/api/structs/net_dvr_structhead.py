from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STRUCTHEAD(Structure):
    pass

_S(struct_tagNET_DVR_STRUCTHEAD, [
    ('wLength', WORD),
    ('byVersion', BYTE),
    ('byRes', BYTE),
])

NET_DVR_STRUCTHEAD = struct_tagNET_DVR_STRUCTHEAD
LPNET_DVR_STRUCTHEAD = POINTER(struct_tagNET_DVR_STRUCTHEAD)
tagNET_DVR_STRUCTHEAD = struct_tagNET_DVR_STRUCTHEAD
