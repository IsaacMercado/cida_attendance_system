from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DIALSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_DIALSTATUS, [
    ('byRealMode', BYTE),
    ('byUimCard', BYTE),
    ('byRes1', BYTE * 6),
    ('dwSignal', DWORD),
    ('dwDialStatus', DWORD),
    ('struLocalIp', NET_DVR_IPADDR),
    ('struRemoteIp', NET_DVR_IPADDR),
    ('struNetMask', NET_DVR_IPADDR),
    ('struDns', NET_DVR_IPADDR),
    ('byRes2', BYTE * 16),
])

NET_DVR_DIALSTATUS = struct_tagNET_DVR_DIALSTATUS
LPNET_DVR_DIALSTATUS = POINTER(struct_tagNET_DVR_DIALSTATUS)
tagNET_DVR_DIALSTATUS = struct_tagNET_DVR_DIALSTATUS
