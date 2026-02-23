from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FILM_MODE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FILM_MODE_CFG, [
    ('dwSize', DWORD),
    ('byScreenType', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_FILM_MODE_CFG = struct_tagNET_DVR_FILM_MODE_CFG
LPNET_DVR_FILM_MODE_CFG = POINTER(struct_tagNET_DVR_FILM_MODE_CFG)
tagNET_DVR_FILM_MODE_CFG = struct_tagNET_DVR_FILM_MODE_CFG
