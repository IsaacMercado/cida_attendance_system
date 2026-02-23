from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SERIALSTART_V40(Structure):
    pass

_S(struct_tagNET_DVR_SERIALSTART_V40, [
    ('dwSize', DWORD),
    ('dwSerialType', DWORD),
    ('bySerialNum', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_SERIALSTART_V40 = struct_tagNET_DVR_SERIALSTART_V40
LPNET_DVR_SERIALSTART_V40 = POINTER(struct_tagNET_DVR_SERIALSTART_V40)
tagNET_DVR_SERIALSTART_V40 = struct_tagNET_DVR_SERIALSTART_V40
