from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEOIN_TYPE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOIN_TYPE_INFO, [
    ('wInType', WORD),
    ('wInNum', WORD),
    ('wStartNo', WORD),
    ('byRes', BYTE * 6),
])

NET_DVR_VIDEOIN_TYPE_INFO = struct_tagNET_DVR_VIDEOIN_TYPE_INFO
LPNET_DVR_VIDEOIN_TYPE_INFO = POINTER(struct_tagNET_DVR_VIDEOIN_TYPE_INFO)
tagNET_DVR_VIDEOIN_TYPE_INFO = struct_tagNET_DVR_VIDEOIN_TYPE_INFO
