from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNet_DVR_TEST_SELFCHECK_RESULT(Structure):
    pass

_S(struct_tagNet_DVR_TEST_SELFCHECK_RESULT, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('bySelfCheckStatus', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_TEST_SELFCHECK_RESULT = struct_tagNet_DVR_TEST_SELFCHECK_RESULT
LPNET_DVR_TEST_SELECHECK_RESULT = POINTER(struct_tagNet_DVR_TEST_SELFCHECK_RESULT)
tagNet_DVR_TEST_SELFCHECK_RESULT = struct_tagNet_DVR_TEST_SELFCHECK_RESULT
