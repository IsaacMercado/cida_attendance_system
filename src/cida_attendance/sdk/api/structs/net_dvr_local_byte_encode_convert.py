from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from ..functions import CHAR_ENCODE_CONVERT


class struct_tagNET_DVR_LOCAL_BYTE_ENCODE_CONVERT(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_BYTE_ENCODE_CONVERT, [
    ('fnCharConvertCallBack', CHAR_ENCODE_CONVERT),
    ('byRes', BYTE * 256),
])

NET_DVR_LOCAL_BYTE_ENCODE_CONVERT = struct_tagNET_DVR_LOCAL_BYTE_ENCODE_CONVERT
LPNET_DVR_LOCAL_BYTE_ENCODE_CONVERT = POINTER(struct_tagNET_DVR_LOCAL_BYTE_ENCODE_CONVERT)
tagNET_DVR_LOCAL_BYTE_ENCODE_CONVERT = struct_tagNET_DVR_LOCAL_BYTE_ENCODE_CONVERT
