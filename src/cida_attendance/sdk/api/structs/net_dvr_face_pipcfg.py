from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACE_PIPCFG(Structure):
    pass

_S(struct_tagNET_DVR_FACE_PIPCFG, [
    ('byEnable', BYTE),
    ('byBackChannel', BYTE),
    ('byPosition', BYTE),
    ('byPIPDiv', BYTE),
    ('byRes', BYTE * 4),
])

NET_DVR_FACE_PIPCFG = struct_tagNET_DVR_FACE_PIPCFG
LPNET_DVR_FACE_PIPCFG = POINTER(struct_tagNET_DVR_FACE_PIPCFG)
tagNET_DVR_FACE_PIPCFG = struct_tagNET_DVR_FACE_PIPCFG
