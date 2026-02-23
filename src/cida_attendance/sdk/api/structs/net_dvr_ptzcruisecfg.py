from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ptzcruise_pointcfg import NET_DVR_PTZCRUISE_POINTCFG


class struct_tagNET_DVR_PTZCRUISECFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZCRUISECFG, [
    ('dwSize', DWORD),
    ('dwCruiseRoute', DWORD),
    ('struCruisePoint', NET_DVR_PTZCRUISE_POINTCFG * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_PTZCRUISECFG = struct_tagNET_DVR_PTZCRUISECFG
LPNET_DVR_PTZCRUISECFG = POINTER(struct_tagNET_DVR_PTZCRUISECFG)
tagNET_DVR_PTZCRUISECFG = struct_tagNET_DVR_PTZCRUISECFG
