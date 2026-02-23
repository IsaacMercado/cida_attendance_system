from ctypes import Structure

from ..base_classes import _S, BYTE
from .net_dvr_single_net_disk_info_v40 import NET_DVR_SINGLE_NET_DISK_INFO_V40


class struct_anon_375(Structure):
    pass

_S(struct_anon_375, [
    ('struNasPara', NET_DVR_SINGLE_NET_DISK_INFO_V40),
    ('byRes1', BYTE * 260),
])

