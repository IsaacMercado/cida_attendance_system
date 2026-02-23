from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LITESTORAGE(Structure):
    pass

_S(struct_tagNET_DVR_LITESTORAGE, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byStorageTime', BYTE),
    ('byLevel', BYTE),
    ('byRes', BYTE),
    ('fCapacity', c_float),
    ('byDefLowStorageTime', BYTE),
    ('byDefMediumStorageTime', BYTE),
    ('byDefHighStorageTime', BYTE),
    ('byRes1', BYTE * 61),
])

NET_DVR_LITESTORAGE = struct_tagNET_DVR_LITESTORAGE
LPNET_DVR_LITESTORAGE = POINTER(struct_tagNET_DVR_LITESTORAGE)
tagNET_DVR_LITESTORAGE = struct_tagNET_DVR_LITESTORAGE
