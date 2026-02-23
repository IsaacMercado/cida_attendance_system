from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PIRIS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PIRIS_PARAM, [
    ('byMode', BYTE),
    ('byPIrisAperture', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_PIRIS_PARAM = struct_tagNET_DVR_PIRIS_PARAM
LPNET_DVR_PIRIS_PARAM = POINTER(struct_tagNET_DVR_PIRIS_PARAM)
tagNET_DVR_PIRIS_PARAM = struct_tagNET_DVR_PIRIS_PARAM
