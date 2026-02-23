from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import String


class struct_anon_62(Structure):
    pass

_S(struct_anon_62, [
    ('dwAlarmChanNum', DWORD),
    ('dwPicLen', DWORD),
    ('byPicURL', BYTE),
    ('byTarget', BYTE),
    ('byRes1', BYTE * 2),
    ('pDataBuff', String),
])

