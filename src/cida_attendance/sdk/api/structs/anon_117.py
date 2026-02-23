from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_116 import NET_DVR_FRAMETYPECODE


class struct_anon_117(Structure):
    pass

_S(struct_anon_117, [
    ('dwSize', DWORD),
    ('sATMIP', c_char * 16),
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
])

NET_DVR_FRAMEFORMAT = struct_anon_117
LPNET_DVR_FRAMEFORMAT = POINTER(struct_anon_117)
