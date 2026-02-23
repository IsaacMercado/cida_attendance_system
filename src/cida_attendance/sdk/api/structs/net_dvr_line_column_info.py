from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LINE_COLUMN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LINE_COLUMN_INFO, [
    ('wLine', WORD),
    ('wColumn', WORD),
])

NET_DVR_LINE_COLUMN_INFO = struct_tagNET_DVR_LINE_COLUMN_INFO
LPNET_DVR_LINE_COLUMN_INFO = POINTER(struct_tagNET_DVR_LINE_COLUMN_INFO)
tagNET_DVR_LINE_COLUMN_INFO = struct_tagNET_DVR_LINE_COLUMN_INFO
