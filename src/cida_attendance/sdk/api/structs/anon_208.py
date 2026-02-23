from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD


class struct_anon_208(Structure):
    pass

_S(struct_anon_208, [
    ('dwKeyLength', DWORD),
    ('sKeyInfo', c_char * 63),
    ('byEncryptType', BYTE),
    ('sNewKeyInfo', c_char * 68),
    ('byKeyType', BYTE),
    ('byRes', BYTE * 7),
])

