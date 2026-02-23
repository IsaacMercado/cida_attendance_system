from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_83(Structure):
    pass

_S(struct_anon_83, [
    ('dwHDNo', DWORD),
    ('dwCapacity', DWORD),
    ('dwFreeSpace', DWORD),
    ('dwHdStatus', DWORD),
    ('byHDAttr', BYTE),
    ('byHDType', BYTE),
    ('byDiskDriver', BYTE),
    ('byRes1', BYTE),
    ('dwHdGroup', DWORD),
    ('byRecycling', BYTE),
    ('bySupportFormatType', BYTE),
    ('byFormatType', BYTE),
    ('byRes2', BYTE),
    ('dwStorageType', DWORD),
    ('dwPictureCapacity', DWORD),
    ('dwFreePictureSpace', DWORD),
    ('byRes3', BYTE * 104),
])

NET_DVR_SINGLE_HD = struct_anon_83
LPNET_DVR_SINGLE_HD = POINTER(struct_anon_83)
