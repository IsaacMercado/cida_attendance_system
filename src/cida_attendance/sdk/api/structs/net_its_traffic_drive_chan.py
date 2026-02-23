from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_TRAFFIC_DRIVE_CHAN(Structure):
    pass

_S(struct_tagNET_ITS_TRAFFIC_DRIVE_CHAN, [
    ('byDriveChan', BYTE),
    ('byRes1', BYTE * 3),
    ('wCarFlux', WORD),
    ('wPasserbyFlux', WORD),
    ('wShayFlux', WORD),
    ('fAverOccpancy', c_float),
    ('wAverSpeed', WORD),
    ('wAverCarDis', WORD),
    ('byRes2', BYTE * 16),
])

NET_ITS_TRAFFIC_DRIVE_CHAN = struct_tagNET_ITS_TRAFFIC_DRIVE_CHAN
LPNET_ITS_TRAFFIC_DRIVE_CHAN = POINTER(struct_tagNET_ITS_TRAFFIC_DRIVE_CHAN)
tagNET_ITS_TRAFFIC_DRIVE_CHAN = struct_tagNET_ITS_TRAFFIC_DRIVE_CHAN
