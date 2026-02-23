from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD


class struct_anon_11(Structure):
    pass

_S(struct_anon_11, [
    ('sDVRIP', c_char * 16),
    ('sDVRIPMask', c_char * 16),
    ('dwNetInterface', DWORD),
    ('wDVRPort', WORD),
    ('byMACAddr', BYTE * 6),
])

NET_DVR_ETHERNET = struct_anon_11
