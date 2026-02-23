from ctypes import Structure, c_char

from ..base_classes import _S, DWORD


class struct_anon_207(Structure):
    pass

_S(struct_anon_207, [
    ('dwAuthentication', DWORD),
    ('dwKeyLength', DWORD),
    ('dwKeyType', DWORD),
    ('dwActive', DWORD),
    ('sKeyInfo', (c_char * 33) * 4),
])

