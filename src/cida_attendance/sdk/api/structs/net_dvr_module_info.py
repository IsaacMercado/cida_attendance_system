from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MODULE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_MODULE_INFO, [
    ('dwSize', DWORD),
    ('byModuleType', BYTE),
    ('byKeyBoardType', BYTE),
    ('byTriggerType', BYTE),
    ('byZoneType', BYTE),
    ('wModuleAddress', WORD),
    ('byRes2', BYTE * 2),
    ('sModelInfo', c_char * 32),
    ('sDeviceVersionInfo', c_char * 32),
    ('byRes', BYTE * 128),
])

NET_DVR_MODULE_INFO = struct_tagNET_DVR_MODULE_INFO
LPNET_DVR_MODULE_INFO = POINTER(struct_tagNET_DVR_MODULE_INFO)
tagNET_DVR_MODULE_INFO = struct_tagNET_DVR_MODULE_INFO
