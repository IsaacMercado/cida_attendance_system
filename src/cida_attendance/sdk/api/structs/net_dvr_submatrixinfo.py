from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SUBMATRIXINFO(Structure):
    pass

_S(struct_tagNET_DVR_SUBMATRIXINFO, [
    ('byMainMatrix', BYTE),
    ('bySubMatrixSequence', BYTE),
    ('byLoginType', BYTE),
    ('byRes1', BYTE * 9),
    ('struSubMatrixIP', NET_DVR_IPADDR),
    ('wSubMatrixPort', WORD),
    ('byRes2', BYTE * 6),
    ('struSubMatrixIPMask', NET_DVR_IPADDR),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('sDomainName', c_char * 64),
    ('sDnsAddress', c_char * 64),
    ('sSerialNumber', BYTE * 48),
    ('byRes3', BYTE * 16),
])

NET_DVR_SUBMATRIXINFO = struct_tagNET_DVR_SUBMATRIXINFO
LPNET_DVR_SUBMATRIXINFO = POINTER(struct_tagNET_DVR_SUBMATRIXINFO)
tagNET_DVR_SUBMATRIXINFO = struct_tagNET_DVR_SUBMATRIXINFO
