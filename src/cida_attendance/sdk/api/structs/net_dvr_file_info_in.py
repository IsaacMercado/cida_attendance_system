from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FILE_INFO_IN(Structure):
    pass

_S(struct_tagNET_DVR_FILE_INFO_IN, [
    ('szFileID', c_char * 128),
    ('byRes', BYTE * 256),
])

NET_DVR_FILE_INFO_IN = struct_tagNET_DVR_FILE_INFO_IN
LPNET_DVR_FILE_INFO_IN = POINTER(struct_tagNET_DVR_FILE_INFO_IN)
tagNET_DVR_FILE_INFO_IN = struct_tagNET_DVR_FILE_INFO_IN
