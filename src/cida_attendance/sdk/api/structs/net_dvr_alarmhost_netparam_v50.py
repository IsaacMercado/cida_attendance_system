from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct__tagNET_DVR_ALARMHOST_NETPARAM_V50(Structure):
    pass

_S(struct__tagNET_DVR_ALARMHOST_NETPARAM_V50, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byAddressType', BYTE),
    ('byEnable', BYTE),
    ('byDomainName', BYTE * 64),
    ('byReportProtocol', BYTE),
    ('byDevID', BYTE * 32),
    ('byProtocolVersion', BYTE),
    ('byRes1', BYTE * 3),
    ('byEHomeKey', BYTE * 32),
    ('byRes2', BYTE * 28),
])

NET_DVR_ALARMHOST_NETPARAM_V50 = struct__tagNET_DVR_ALARMHOST_NETPARAM_V50
LPNET_DVR_ALARMHOST_NETPARAM_V50 = POINTER(struct__tagNET_DVR_ALARMHOST_NETPARAM_V50)
_tagNET_DVR_ALARMHOST_NETPARAM_V50 = struct__tagNET_DVR_ALARMHOST_NETPARAM_V50
