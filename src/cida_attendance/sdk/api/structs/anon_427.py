from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from .anon_2 import NET_DVR_IPADDR


class struct_anon_427(Structure):
    pass

_S(struct_anon_427, [
    ('byExternalMode', BYTE),
    ('byRes', BYTE * 3),
    ('struDevIP', NET_DVR_IPADDR),
    ('wDevPort', WORD),
    ('byRs485No', BYTE),
    ('byDevCtrlCode', BYTE),
    ('byCtrlCardType', BYTE),
    ('byLedScreenType', BYTE),
    ('byLedScreenUse', BYTE),
    ('byLedDisplayMode', BYTE),
    ('sLedCustomInfo', c_char * 256),
    ('dwLedScreenH', DWORD),
    ('dwLedScreenW', DWORD),
    ('byRes1', BYTE * 236),
])

