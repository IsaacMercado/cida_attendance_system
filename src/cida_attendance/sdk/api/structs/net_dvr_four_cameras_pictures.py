from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FOUR_CAMERAS_PICTURES(Structure):
    pass

_S(struct_tagNET_DVR_FOUR_CAMERAS_PICTURES, [
    ('dwSize', DWORD),
    ('dwFileLen', DWORD),
    ('byChannel', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_FOUR_CAMERAS_PICTURES = struct_tagNET_DVR_FOUR_CAMERAS_PICTURES
LPNET_DVR_FOUR_CAMERAS_PICTURES = POINTER(struct_tagNET_DVR_FOUR_CAMERAS_PICTURES)
tagNET_DVR_FOUR_CAMERAS_PICTURES = struct_tagNET_DVR_FOUR_CAMERAS_PICTURES
