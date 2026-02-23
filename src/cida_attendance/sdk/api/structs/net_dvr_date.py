from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DATE_(Structure):
    pass

_S(struct_tagNET_DVR_DATE_, [
    ('wYear', WORD),
    ('byMonth', BYTE),
    ('byDay', BYTE),
])

NET_DVR_DATE = struct_tagNET_DVR_DATE_
LPNET_DVR_DATE = POINTER(struct_tagNET_DVR_DATE_)
tagNET_DVR_DATE_ = struct_tagNET_DVR_DATE_
