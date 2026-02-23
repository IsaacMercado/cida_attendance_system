from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_108(Structure):
    pass

_S(struct_anon_108, [
    ('byRecordStatic', BYTE),
    ('bySignalStatic', BYTE),
    ('byHardwareStatic', BYTE),
    ('byRes1', BYTE),
    ('dwBitRate', DWORD),
    ('dwLinkNum', DWORD),
    ('struClientIP', NET_DVR_IPADDR * 6),
    ('dwIPLinkNum', DWORD),
    ('byExceedMaxLink', BYTE),
    ('byRes', BYTE * 3),
    ('dwAllBitRate', DWORD),
    ('dwChannelNo', DWORD),
])

NET_DVR_CHANNELSTATE_V30 = struct_anon_108
LPNET_DVR_CHANNELSTATE_V30 = POINTER(struct_anon_108)
