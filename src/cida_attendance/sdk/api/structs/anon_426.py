from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_426(Structure):
    pass

_S(struct_anon_426, [
    ('byRs485No', BYTE),
    ('byDevCtrlCode', BYTE),
    ('byAutoIssuedData', BYTE),
    ('byOfflineDetEnable', BYTE),
    ('byDetCycle', BYTE),
    ('byRes', BYTE * 651),
])

