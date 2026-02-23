from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXTERNAL_DEVCOND(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_DEVCOND, [
    ('dwSize', DWORD),
    ('byExternalDevTpye', BYTE),
    ('byRelativeIndex', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_EXTERNAL_DEVCOND = struct_tagNET_DVR_EXTERNAL_DEVCOND
LPNET_DVR_EXTERNAL_DEVCOND = POINTER(struct_tagNET_DVR_EXTERNAL_DEVCOND)
tagNET_DVR_EXTERNAL_DEVCOND = struct_tagNET_DVR_EXTERNAL_DEVCOND
