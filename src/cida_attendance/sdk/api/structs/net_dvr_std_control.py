from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STD_CONTROL(Structure):
    pass

_S(struct_tagNET_DVR_STD_CONTROL, [
    ('lpCondBuffer', POINTER(None)),
    ('dwCondSize', DWORD),
    ('lpStatusBuffer', POINTER(None)),
    ('dwStatusSize', DWORD),
    ('lpXmlBuffer', POINTER(None)),
    ('dwXmlSize', DWORD),
    ('byDataType', BYTE),
    ('byRes', BYTE * 55),
])

NET_DVR_STD_CONTROL = struct_tagNET_DVR_STD_CONTROL
LPNET_DVR_STD_CONTROL = POINTER(struct_tagNET_DVR_STD_CONTROL)
tagNET_DVR_STD_CONTROL = struct_tagNET_DVR_STD_CONTROL
