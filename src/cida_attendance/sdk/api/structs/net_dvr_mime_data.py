from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MIME_DATA(Structure):
    pass

_S(struct_tagNET_DVR_MIME_DATA, [
    ('byContentType', BYTE),
    ('byRes1', BYTE * 3),
    ('lpContent', POINTER(None)),
    ('dwContentSize', DWORD),
    ('sContentID', c_char * 32),
    ('byRes', BYTE * 512),
])

NET_DVR_MIME_DATA = struct_tagNET_DVR_MIME_DATA
LPNET_DVR_MIME_DATA = POINTER(struct_tagNET_DVR_MIME_DATA)
tagNET_DVR_MIME_DATA = struct_tagNET_DVR_MIME_DATA
