from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_2 import NET_DVR_IPADDR


class struct_anon_378(Structure):
    pass

_S(struct_anon_378, [
    ('struIp', NET_DVR_IPADDR),
    ('byRes1', BYTE * 716),
])

