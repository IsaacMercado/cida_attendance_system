from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_449(Structure):
    pass

_S(struct_anon_449, [
    ('dwSize', DWORD),
    ('byStatus', BYTE),
    ('byMasterSlaveProperty', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_NS_RING_STATUS = struct_anon_449
LPNET_DVR_NS_RING_STATUS = POINTER(struct_anon_449)
