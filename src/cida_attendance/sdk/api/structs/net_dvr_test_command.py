from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEST_COMMAND(Structure):
    pass

_S(struct_tagNET_DVR_TEST_COMMAND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byTestCommand', BYTE * 32),
    ('wICRIntervalTime', WORD),
    ('byElectronicCompassState', BYTE),
    ('byRes1', BYTE * 1),
    ('fDeviceTem', c_float),
    ('byTemp', BYTE * 9),
    ('byRes', BYTE * 3),
])

NET_DVR_TEST_COMMAND = struct_tagNET_DVR_TEST_COMMAND
LPNET_DVR_TEST_COMMAND = POINTER(struct_tagNET_DVR_TEST_COMMAND)
tagNET_DVR_TEST_COMMAND = struct_tagNET_DVR_TEST_COMMAND
