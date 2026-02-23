from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MANUALSNAP(Structure):
    pass

_S(struct_tagNET_DVR_MANUALSNAP, [
    ('byOSDEnable', BYTE),
    ('byLaneNo', BYTE),
    ('byChannel', BYTE),
    ('byRes', BYTE * 21),
])

NET_DVR_MANUALSNAP = struct_tagNET_DVR_MANUALSNAP
LPNET_DVR_MANUALSNAP = POINTER(struct_tagNET_DVR_MANUALSNAP)
tagNET_DVR_MANUALSNAP = struct_tagNET_DVR_MANUALSNAP
