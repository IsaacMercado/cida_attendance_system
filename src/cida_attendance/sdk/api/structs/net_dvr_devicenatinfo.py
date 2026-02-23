from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEVICENATINFO(Structure):
    pass

_S(struct_tagNET_DVR_DEVICENATINFO, [
    ('struPuIp', NET_DVR_IPADDR),
    ('wOuterPort', WORD),
    ('wInterPort', WORD),
    ('nSessionID', DWORD),
    ('byRes', BYTE * 4),
])

NET_DVR_DEVICENATINFO = struct_tagNET_DVR_DEVICENATINFO
LPNET_DVR_DEVICENATINFO = POINTER(struct_tagNET_DVR_DEVICENATINFO)
tagNET_DVR_DEVICENATINFO = struct_tagNET_DVR_DEVICENATINFO
