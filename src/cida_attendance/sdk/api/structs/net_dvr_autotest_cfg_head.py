from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUTOTEST_CFG_HEAD(Structure):
    pass

_S(struct_tagNET_DVR_AUTOTEST_CFG_HEAD, [
    ('dwSize', DWORD),
    ('dwInfoType', DWORD),
    ('dwRetResult', DWORD),
    ('dwDataBodySize', DWORD),
    ('lpDataBody', POINTER(None)),
    ('byRes', BYTE * 32),
])

NET_DVR_AUTOTEST_CFG_HEAD = struct_tagNET_DVR_AUTOTEST_CFG_HEAD
LPNET_DVR_AUTOTEST_CFG_HEAD = POINTER(struct_tagNET_DVR_AUTOTEST_CFG_HEAD)
tagNET_DVR_AUTOTEST_CFG_HEAD = struct_tagNET_DVR_AUTOTEST_CFG_HEAD
