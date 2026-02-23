from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_MESSAGE(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_MESSAGE, [
    ('sMessage', c_char * 44),
    ('byRes', BYTE * 46),
])

NET_DVR_INQUEST_MESSAGE = struct_tagNET_DVR_INQUEST_MESSAGE
LPNET_DVR_INQUEST_MESSAGE = POINTER(struct_tagNET_DVR_INQUEST_MESSAGE)
tagNET_DVR_INQUEST_MESSAGE = struct_tagNET_DVR_INQUEST_MESSAGE
