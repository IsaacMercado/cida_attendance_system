from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_mb_ipaddr import NET_DVR_MB_IPADDR


class struct_tagNET_DVR_MB_WVSPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_WVSPARA, [
    ('struWVSAddr', NET_DVR_MB_IPADDR),
    ('byPuid', BYTE * 32),
    ('byPassword', BYTE * 16),
    ('byRes', BYTE * 8),
])

NET_DVR_MB_WVSPARA = struct_tagNET_DVR_MB_WVSPARA
LPNET_DVR_MB_WVSPARA = POINTER(struct_tagNET_DVR_MB_WVSPARA)
tagNET_DVR_MB_WVSPARA = struct_tagNET_DVR_MB_WVSPARA
