from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_109(Structure):
    pass

_S(struct_anon_109, [
    ('byRecordStatic', BYTE),
    ('bySignalStatic', BYTE),
    ('byHardwareStatic', BYTE),
    ('reservedData', c_char),
    ('dwBitRate', DWORD),
    ('dwLinkNum', DWORD),
    ('dwClientIP', DWORD * 6),
])

NET_DVR_CHANNELSTATE = struct_anon_109
LPNET_DVR_CHANNELSTATE = POINTER(struct_anon_109)
