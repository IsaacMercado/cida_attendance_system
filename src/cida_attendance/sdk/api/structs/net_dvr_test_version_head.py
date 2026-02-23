from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEST_VERSION_HEAD(Structure):
    pass

_S(struct_tagNET_DVR_TEST_VERSION_HEAD, [
    ('dwSize', DWORD),
    ('dwParam1', DWORD),
    ('byParam2', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_TEST_VERSION_HEAD = struct_tagNET_DVR_TEST_VERSION_HEAD
LPNET_DVR_TEST_VERSION_HEAD = POINTER(struct_tagNET_DVR_TEST_VERSION_HEAD)
tagNET_DVR_TEST_VERSION_HEAD = struct_tagNET_DVR_TEST_VERSION_HEAD
