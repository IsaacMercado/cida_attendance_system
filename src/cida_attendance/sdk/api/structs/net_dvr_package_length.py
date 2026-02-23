from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_116 import NET_DVR_FRAMETYPECODE


class struct_tagNET_DVR_PACKAGE_LENGTH(Structure):
    pass

_S(struct_tagNET_DVR_PACKAGE_LENGTH, [
    ('byLengthMode', BYTE),
    ('byRes1', BYTE * 3),
    ('dwFixLength', DWORD),
    ('dwMaxLength', DWORD),
    ('dwMinLength', DWORD),
    ('byEndMode', BYTE),
    ('byRes2', BYTE * 3),
    ('struEndCode', NET_DVR_FRAMETYPECODE),
    ('dwLengthPos', DWORD),
    ('dwLengthLen', DWORD),
    ('byRes3', BYTE * 8),
])

NET_DVR_PACKAGE_LENGTH = struct_tagNET_DVR_PACKAGE_LENGTH
LPNET_DVR_PACKAGE_LENGTH = POINTER(struct_tagNET_DVR_PACKAGE_LENGTH)
tagNET_DVR_PACKAGE_LENGTH = struct_tagNET_DVR_PACKAGE_LENGTH
