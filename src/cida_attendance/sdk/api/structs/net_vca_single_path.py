from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_SINGLE_PATH(Structure):
    pass

_S(struct_tagNET_VCA_SINGLE_PATH, [
    ('byActive', BYTE),
    ('byType', BYTE),
    ('bySaveAlarmPic', BYTE),
    ('byRes1', BYTE * 5),
    ('dwDiskDriver', DWORD),
    ('dwLeftSpace', DWORD),
    ('byRes2', BYTE * 8),
])

NET_VCA_SINGLE_PATH = struct_tagNET_VCA_SINGLE_PATH
LPNET_VCA_SINGLE_PATH = POINTER(struct_tagNET_VCA_SINGLE_PATH)
tagNET_VCA_SINGLE_PATH = struct_tagNET_VCA_SINGLE_PATH
