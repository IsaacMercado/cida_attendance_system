from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ANTI_SNEAK_HOST_READER_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ANTI_SNEAK_HOST_READER_INFO, [
    ('byAntiSnealHostNo', BYTE),
    ('byRes', BYTE * 5),
    ('wFollowUpCardReader', WORD),
])

NET_DVR_ANTI_SNEAK_HOST_READER_INFO = struct_tagNET_DVR_ANTI_SNEAK_HOST_READER_INFO
LPNET_DVR_ANTI_SNEAK_HOST_READER_INFO = POINTER(struct_tagNET_DVR_ANTI_SNEAK_HOST_READER_INFO)
tagNET_DVR_ANTI_SNEAK_HOST_READER_INFO = struct_tagNET_DVR_ANTI_SNEAK_HOST_READER_INFO
