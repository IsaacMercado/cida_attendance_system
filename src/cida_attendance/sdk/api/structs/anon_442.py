from ctypes import Structure

from ..base_classes import _S
from .anon_2 import NET_DVR_IPADDR


class struct_anon_442(Structure):
    pass

_S(struct_anon_442, [
    ('struIp', NET_DVR_IPADDR),
])

