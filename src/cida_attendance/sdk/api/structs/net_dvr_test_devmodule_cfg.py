from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEST_DEVMODULE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TEST_DEVMODULE_CFG, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byDevFanModuleType', BYTE * 8),
    ('byDevHeaterModuleType', BYTE * 8),
    ('byRes', BYTE * 22),
])

NET_DVR_TEST_DEVMODULE_CFG = struct_tagNET_DVR_TEST_DEVMODULE_CFG
LPNET_DVR_TEST_DEVMODULE_CFG = POINTER(struct_tagNET_DVR_TEST_DEVMODULE_CFG)
tagNET_DVR_TEST_DEVMODULE_CFG = struct_tagNET_DVR_TEST_DEVMODULE_CFG
