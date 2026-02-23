from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .anon_116 import NET_DVR_FRAMETYPECODE


class struct_anon_118(Structure):
    pass

_S(struct_anon_118, [
    ('dwSize', DWORD),
    ('struATMIP', NET_DVR_IPADDR),
    ('dwATMType', DWORD),
    ('dwInputMode', DWORD),
    ('dwFrameSignBeginPos', DWORD),
    ('dwFrameSignLength', DWORD),
    ('byFrameSignContent', BYTE * 12),
    ('dwCardLengthInfoBeginPos', DWORD),
    ('dwCardLengthInfoLength', DWORD),
    ('dwCardNumberInfoBeginPos', DWORD),
    ('dwCardNumberInfoLength', DWORD),
    ('dwBusinessTypeBeginPos', DWORD),
    ('dwBusinessTypeLength', DWORD),
    ('frameTypeCode', NET_DVR_FRAMETYPECODE * 10),
    ('wATMPort', WORD),
    ('wProtocolType', WORD),
    ('byRes', BYTE * 24),
])

NET_DVR_FRAMEFORMAT_V30 = struct_anon_118
LPNET_DVR_FRAMEFORMAT_V30 = POINTER(struct_anon_118)
