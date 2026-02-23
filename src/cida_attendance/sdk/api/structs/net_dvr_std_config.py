from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STD_CONFIG(Structure):
    pass

_S(struct_tagNET_DVR_STD_CONFIG, [
    ('lpCondBuffer', POINTER(None)),
    ('dwCondSize', DWORD),
    ('lpInBuffer', POINTER(None)),
    ('dwInSize', DWORD),
    ('lpOutBuffer', POINTER(None)),
    ('dwOutSize', DWORD),
    ('lpStatusBuffer', POINTER(None)),
    ('dwStatusSize', DWORD),
    ('lpXmlBuffer', POINTER(None)),
    ('dwXmlSize', DWORD),
    ('byDataType', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_STD_CONFIG = struct_tagNET_DVR_STD_CONFIG
LPNET_DVR_STD_CONFIG = POINTER(struct_tagNET_DVR_STD_CONFIG)
tagNET_DVR_STD_CONFIG = struct_tagNET_DVR_STD_CONFIG
