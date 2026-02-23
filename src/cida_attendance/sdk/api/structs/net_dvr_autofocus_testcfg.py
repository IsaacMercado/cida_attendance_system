from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUTOFOCUS_TESTCFG(Structure):
    pass

_S(struct_tagNET_DVR_AUTOFOCUS_TESTCFG, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 24),
])

NET_DVR_AUTOFOCUS_TESTCFG = struct_tagNET_DVR_AUTOFOCUS_TESTCFG
LPNET_DVR_AUTOFOCUS_TESTCFG = POINTER(struct_tagNET_DVR_AUTOFOCUS_TESTCFG)
tagNET_DVR_AUTOFOCUS_TESTCFG = struct_tagNET_DVR_AUTOFOCUS_TESTCFG
