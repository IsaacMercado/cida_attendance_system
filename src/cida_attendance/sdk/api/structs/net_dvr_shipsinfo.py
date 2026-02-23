from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_SHIPSINFO(Structure):
    pass

_S(struct_tagNET_DVR_SHIPSINFO, [
    ('fShipsLength', c_float),
    ('fShipsHeight', c_float),
    ('fShipsWidth', c_float),
    ('fShipsSpeed', c_float),
    ('byShipsDirection', BYTE),
    ('byShipsDetState', BYTE),
    ('byTriggerLineID', BYTE),
    ('byRes', BYTE * 61),
    ('struShipsRect', NET_VCA_POLYGON),
])

NET_DVR_SHIPSINFO = struct_tagNET_DVR_SHIPSINFO
LPNET_DVR_SHIPSINFO = POINTER(struct_tagNET_DVR_SHIPSINFO)
tagNET_DVR_SHIPSINFO = struct_tagNET_DVR_SHIPSINFO
