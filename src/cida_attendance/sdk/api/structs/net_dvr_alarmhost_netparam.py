from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ALARMHOST_NETPARAM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_NETPARAM, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byAddressType', BYTE),
    ('byRes1', BYTE * 1),
    ('byDomainName', BYTE * 64),
    ('byReportProtocol', BYTE),
    ('byDevID', BYTE * 32),
    ('byRes2', BYTE * 7),
])

NET_DVR_ALARMHOST_NETPARAM = struct_tagNET_DVR_ALARMHOST_NETPARAM
LPNET_DVR_ALARMHOST_NETPARAM = POINTER(struct_tagNET_DVR_ALARMHOST_NETPARAM)
tagNET_DVR_ALARMHOST_NETPARAM = struct_tagNET_DVR_ALARMHOST_NETPARAM
