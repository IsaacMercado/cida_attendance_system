from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PU_STREAM_URL(Structure):
    pass

_S(struct_tagNET_DVR_PU_STREAM_URL, [
    ('byEnable', BYTE),
    ('strURL', BYTE * 240),
    ('byTransPortocol', BYTE),
    ('wIPID', WORD),
    ('byChannel', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_PU_STREAM_URL = struct_tagNET_DVR_PU_STREAM_URL
LPNET_DVR_PU_STREAM_URL = POINTER(struct_tagNET_DVR_PU_STREAM_URL)
tagNET_DVR_PU_STREAM_URL = struct_tagNET_DVR_PU_STREAM_URL
