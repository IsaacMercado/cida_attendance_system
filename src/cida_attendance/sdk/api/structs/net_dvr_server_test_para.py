from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_381 import union_anon_381


class struct_tagNET_DVR_SERVER_TEST_PARA(Structure):
    pass

_S(struct_tagNET_DVR_SERVER_TEST_PARA, [
    ('dwSize', DWORD),
    ('unionServerPara', union_anon_381),
    ('byRes2', BYTE * 800),
])

NET_DVR_SERVER_TEST_PARA = struct_tagNET_DVR_SERVER_TEST_PARA
LPNET_DVR_SERVER_TEST_PARA = POINTER(struct_tagNET_DVR_SERVER_TEST_PARA)
tagNET_DVR_SERVER_TEST_PARA = struct_tagNET_DVR_SERVER_TEST_PARA
