from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FLOW_TEST_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_FLOW_TEST_PARAM, [
    ('dwSize', DWORD),
    ('lCardIndex', LONG),
    ('dwInterval', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_FLOW_TEST_PARAM = struct_tagNET_DVR_FLOW_TEST_PARAM
LPNET_DVR_FLOW_TEST_PARAM = POINTER(struct_tagNET_DVR_FLOW_TEST_PARAM)
tagNET_DVR_FLOW_TEST_PARAM = struct_tagNET_DVR_FLOW_TEST_PARAM
