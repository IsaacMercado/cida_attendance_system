from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_116 import NET_DVR_FRAMETYPECODE


class struct_tagNET_DVR_PACKAGE_LOCATION(Structure):
    pass

_S(struct_tagNET_DVR_PACKAGE_LOCATION, [
    ('byOffsetMode', BYTE),
    ('byRes1', BYTE * 3),
    ('dwOffsetPos', DWORD),
    ('struTokenCode', NET_DVR_FRAMETYPECODE),
    ('byMultiplierValue', BYTE),
    ('byEternOffset', BYTE),
    ('byCodeMode', BYTE),
    ('byRes2', BYTE * 9),
])

NET_DVR_PACKAGE_LOCATION = struct_tagNET_DVR_PACKAGE_LOCATION
LPNET_DVR_PACKAGE_LOCATION = POINTER(struct_tagNET_DVR_PACKAGE_LOCATION)
tagNET_DVR_PACKAGE_LOCATION = struct_tagNET_DVR_PACKAGE_LOCATION
