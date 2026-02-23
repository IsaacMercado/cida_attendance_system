from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEST_VERSION_HEAD_V2(Structure):
    pass

_S(struct_tagNET_DVR_TEST_VERSION_HEAD_V2, [
    ('dwSize', DWORD),
    ('dwParam1', DWORD),
    ('byParam2', BYTE),
    ('byRes', BYTE * 31),
    ('dwParam1_1', DWORD),
    ('byParam1_2', BYTE),
    ('byRes1', BYTE * 31),
    ('dwParam2_1', DWORD),
    ('byParam2_2', BYTE),
    ('byRes2', BYTE * 31),
])

NET_DVR_TEST_VERSION_HEAD_V2 = struct_tagNET_DVR_TEST_VERSION_HEAD_V2
LPNET_DVR_TEST_VERSION_HEAD_V2 = POINTER(struct_tagNET_DVR_TEST_VERSION_HEAD_V2)
tagNET_DVR_TEST_VERSION_HEAD_V2 = struct_tagNET_DVR_TEST_VERSION_HEAD_V2
