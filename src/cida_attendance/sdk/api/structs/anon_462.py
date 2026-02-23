from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD


class struct_anon_462(Structure):
    pass

_S(struct_anon_462, [
    ('dwPlaylistNo', DWORD),
    ('byPlaylistName', BYTE * 32),
    ('wPlayIndex', WORD),
    ('byPlayType', BYTE),
    ('byRes', BYTE * 3),
    ('dwPlayItem', DWORD),
    ('byPlayItemName', BYTE * 32),
    ('byRes2', BYTE * 16),
])

