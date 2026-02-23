from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_450(Structure):
    pass

_S(struct_anon_450, [
    ('dwChannelNo', DWORD),
    ('byRes', BYTE * 508),
])

