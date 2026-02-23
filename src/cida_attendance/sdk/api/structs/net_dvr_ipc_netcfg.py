from ctypes import Structure, c_char

from ..base_classes import _S, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_IPC_NETCFG(Structure):
    pass

_S(struct_tagNET_DVR_IPC_NETCFG, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('res', c_char * 126),
])

NET_DVR_IPC_NETCFG = struct_tagNET_DVR_IPC_NETCFG
LPNET_DVR_IPC_NETCFG = POINTER(struct_tagNET_DVR_IPC_NETCFG)
tagNET_DVR_IPC_NETCFG = struct_tagNET_DVR_IPC_NETCFG
