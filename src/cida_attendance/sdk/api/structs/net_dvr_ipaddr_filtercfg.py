from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IPADDR_FILTERCFG(Structure):
    pass

_S(struct_tagNET_DVR_IPADDR_FILTERCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byFilterType', BYTE),
    ('byRes1', BYTE * 2),
    ('byRes', BYTE * 16),
    ('byIPAddr', BYTE * 1024),
])

NET_DVR_IPADDR_FILTERCFG = struct_tagNET_DVR_IPADDR_FILTERCFG
LPNET_DVR_IPADDR_FILTERCFG = POINTER(struct_tagNET_DVR_IPADDR_FILTERCFG)
tagNET_DVR_IPADDR_FILTERCFG = struct_tagNET_DVR_IPADDR_FILTERCFG
