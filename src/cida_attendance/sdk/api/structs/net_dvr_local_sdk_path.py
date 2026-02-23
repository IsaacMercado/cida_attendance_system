from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_SDK_PATH(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_SDK_PATH, [
    ('sPath', c_char * 256),
    ('byRes', BYTE * 128),
])

NET_DVR_LOCAL_SDK_PATH = struct_tagNET_DVR_LOCAL_SDK_PATH
LPNET_DVR_LOCAL_SDK_PATH = POINTER(struct_tagNET_DVR_LOCAL_SDK_PATH)
tagNET_DVR_LOCAL_SDK_PATH = struct_tagNET_DVR_LOCAL_SDK_PATH
