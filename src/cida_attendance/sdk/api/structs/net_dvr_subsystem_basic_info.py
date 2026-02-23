from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SUBSYSTEM_BASIC_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEM_BASIC_INFO, [
    ('dwSize', DWORD),
    ('bySubSystemType', BYTE),
    ('bySubSystemNo', BYTE),
    ('byInterfaceType', BYTE),
    ('byRes1', BYTE),
    ('dwChan', DWORD),
    ('struSubSystemIP', NET_DVR_IPADDR),
    ('struSubSystemIPMask', NET_DVR_IPADDR),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('wSubSystemPort', WORD),
    ('byRes2', BYTE * 6),
    ('sSerialNumber', BYTE * 48),
    ('byBelongBoard', BYTE),
    ('byBelongBoardH', BYTE),
    ('byRes3', BYTE * 2),
    ('byDeviceName', BYTE * 20),
    ('dwStartChanNo', DWORD),
    ('byDevNo', BYTE),
    ('byRes4', BYTE * 63),
])

NET_DVR_SUBSYSTEM_BASIC_INFO = struct_tagNET_DVR_SUBSYSTEM_BASIC_INFO
LPNET_DVR_SUBSYSTEM_BASIC_INFO = POINTER(struct_tagNET_DVR_SUBSYSTEM_BASIC_INFO)
tagNET_DVR_SUBSYSTEM_BASIC_INFO = struct_tagNET_DVR_SUBSYSTEM_BASIC_INFO
