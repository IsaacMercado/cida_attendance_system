from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_14 import NET_DVR_ETHERNET_MULTI


class struct_tagNET_DVR_SUBSYSTEM_NETCFG(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEM_NETCFG, [
    ('dwSize', DWORD),
    ('byDefaultRoute', BYTE),
    ('byNetworkCardNum', BYTE),
    ('byCurDetectType', BYTE),
    ('byRes1', BYTE),
    ('struEtherNet', NET_DVR_ETHERNET_MULTI * 4),
    ('byRes2', BYTE * 128),
])

NET_DVR_SUBSYSTEM_NETCFG = struct_tagNET_DVR_SUBSYSTEM_NETCFG
LPNET_DVR_SUBSYSTEM_NETCFG = POINTER(struct_tagNET_DVR_SUBSYSTEM_NETCFG)
tagNET_DVR_SUBSYSTEM_NETCFG = struct_tagNET_DVR_SUBSYSTEM_NETCFG
