from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_85(Structure):
    pass

_S(struct_anon_85, [
    ('dwHDNo', DWORD),
    ('dwCapacity', DWORD),
    ('dwFreeSpace', DWORD),
    ('dwHdStatus', DWORD),
    ('byHDAttr', BYTE),
    ('byHDType', BYTE),
    ('byDiskDriver', BYTE),
    ('byGenusGruop', BYTE),
    ('dwHdGroup', DWORD),
    ('byRecycling', BYTE),
    ('bySupportFormatType', BYTE),
    ('byFormatType', BYTE),
    ('byRes2', BYTE),
    ('dwStorageType', DWORD),
    ('dwPictureCapacity', DWORD),
    ('dwFreePictureSpace', DWORD),
    ('byDiskLocation', BYTE * 16),
    ('bySupplierName', BYTE * 32),
    ('byDiskModel', BYTE * 64),
    ('szHDLocateIP', c_char * 48),
    ('byRes3', BYTE * 80),
])

NET_DVR_SINGLE_HD_V50 = struct_anon_85
LPNET_DVR_SINGLE_HD_V50 = POINTER(struct_anon_85)
