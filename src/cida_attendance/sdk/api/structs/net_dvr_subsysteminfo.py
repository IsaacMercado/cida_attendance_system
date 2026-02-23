from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SUBSYSTEMINFO(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEMINFO, [
    ('bySubSystemType', BYTE),
    ('byChan', BYTE),
    ('byLoginType', BYTE),
    ('byRes1', BYTE * 5),
    ('struSubSystemIP', NET_DVR_IPADDR),
    ('wSubSystemPort', WORD),
    ('byRes2', BYTE * 6),
    ('struSubSystemIPMask', NET_DVR_IPADDR),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('sDomainName', c_char * 64),
    ('sDnsAddress', c_char * 64),
    ('sSerialNumber', BYTE * 48),
])

NET_DVR_SUBSYSTEMINFO = struct_tagNET_DVR_SUBSYSTEMINFO
LPNET_DVR_SUBSYSTEMINFO = POINTER(struct_tagNET_DVR_SUBSYSTEMINFO)
tagNET_DVR_SUBSYSTEMINFO = struct_tagNET_DVR_SUBSYSTEMINFO
