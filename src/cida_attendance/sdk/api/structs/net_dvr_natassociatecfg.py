from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_13 import NET_DVR_NETCFG_V30


class struct_tagNET_DVR_NATASSOCIATECFG(Structure):
    pass

_S(struct_tagNET_DVR_NATASSOCIATECFG, [
    ('dwSize', DWORD),
    ('struNatIpAddress', NET_DVR_NETCFG_V30 * 2),
    ('byNATEnable', BYTE),
    ('byNATCfgMode', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_NATASSOCIATECFG = struct_tagNET_DVR_NATASSOCIATECFG
LPNET_DVR_NATASSOCIATECFG = POINTER(struct_tagNET_DVR_NATASSOCIATECFG)
tagNET_DVR_NATASSOCIATECFG = struct_tagNET_DVR_NATASSOCIATECFG
