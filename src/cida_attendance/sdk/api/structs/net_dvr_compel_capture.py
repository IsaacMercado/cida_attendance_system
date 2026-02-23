from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_COMPEL_CAPTURE(Structure):
    pass

_S(struct_tagNET_DVR_COMPEL_CAPTURE, [
    ('dwSize', DWORD),
    ('byParkIndex', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_COMPEL_CAPTURE = struct_tagNET_DVR_COMPEL_CAPTURE
LPNET_DVR_COMPEL_CAPTURE = POINTER(struct_tagNET_DVR_COMPEL_CAPTURE)
tagNET_DVR_COMPEL_CAPTURE = struct_tagNET_DVR_COMPEL_CAPTURE
