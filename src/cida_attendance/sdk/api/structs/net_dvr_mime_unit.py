from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_MIME_UNIT(Structure):
    pass

_S(struct_tagNET_DVR_MIME_UNIT, [
    ('szContentType', c_char * 32),
    ('szName', c_char * 256),
    ('szFilename', c_char * 256),
    ('dwContentLen', DWORD),
    ('pContent', String),
    ('bySelfRead', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_MIME_UNIT = struct_tagNET_DVR_MIME_UNIT
LPNET_DVR_MIME_UNIT = POINTER(struct_tagNET_DVR_MIME_UNIT)
tagNET_DVR_MIME_UNIT = struct_tagNET_DVR_MIME_UNIT
