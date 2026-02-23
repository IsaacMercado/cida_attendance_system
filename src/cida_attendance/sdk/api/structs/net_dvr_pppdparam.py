from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PPPDPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PPPDPARAM, [
    ('byDialNum', BYTE * 32),
    ('byUserName', BYTE * 32),
    ('byPassword', BYTE * 32),
    ('byApn', BYTE * 32),
    ('struLocalIp', NET_DVR_IPADDR),
    ('struRemoteIp', NET_DVR_IPADDR),
    ('wMtuSize', WORD),
    ('byVerifyProtocal', BYTE),
    ('byRes', BYTE * 25),
])

NET_DVR_PPPDPARAM = struct_tagNET_DVR_PPPDPARAM
LPNET_DVR_PPPDPARAM = POINTER(struct_tagNET_DVR_PPPDPARAM)
tagNET_DVR_PPPDPARAM = struct_tagNET_DVR_PPPDPARAM
