from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_447(Structure):
    pass

_S(struct_anon_447, [
    ('byPort', BYTE),
    ('byMasterSlaveProperty', BYTE),
    ('byPortEthernetType', BYTE),
    ('byRes', BYTE * 9),
])

NET_DVR_RING_PORT_PROPERTY = struct_anon_447
LPNET_DVR_RING_PORT_PROPERTY = POINTER(struct_anon_447)
