from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEST_SPOTCFG(Structure):
    pass

_S(struct_tagNET_DVR_TEST_SPOTCFG, [
    ('dwSize', DWORD),
    ('byStepCount', BYTE),
    ('byStepIndex', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_TEST_SPOTCFG = struct_tagNET_DVR_TEST_SPOTCFG
LPNET_DVR_TEST_SPOTCFG = POINTER(struct_tagNET_DVR_TEST_SPOTCFG)
tagNET_DVR_TEST_SPOTCFG = struct_tagNET_DVR_TEST_SPOTCFG
