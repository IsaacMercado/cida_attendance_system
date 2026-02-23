from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_VIS_REGISTER_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VIS_REGISTER_INFO, [
    ('dwSize', DWORD),
    ('dwID', DWORD),
    ('szDevNumber', BYTE * 32),
    ('byMACAddr', BYTE * 6),
    ('byRes1', BYTE * 2),
    ('sSerialNumber', BYTE * 48),
    ('struDevIP', NET_DVR_IPADDR),
    ('struRegisterTime', NET_DVR_TIME_EX),
    ('byRegisterType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_VIS_REGISTER_INFO = struct_tagNET_DVR_VIS_REGISTER_INFO
LPNET_DVR_VIS_REGISTER_INFO = POINTER(struct_tagNET_DVR_VIS_REGISTER_INFO)
tagNET_DVR_VIS_REGISTER_INFO = struct_tagNET_DVR_VIS_REGISTER_INFO
