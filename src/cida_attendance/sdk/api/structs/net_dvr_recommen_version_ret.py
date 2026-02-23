from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECOMMEN_VERSION_RET(Structure):
    pass

_S(struct_tagNET_DVR_RECOMMEN_VERSION_RET, [
    ('dwSize', DWORD),
    ('byRecommenUpgrade', BYTE),
    ('byRes', BYTE * 123),
])

NET_DVR_RECOMMEN_VERSION_RET = struct_tagNET_DVR_RECOMMEN_VERSION_RET
LPNET_DVR_RECOMMEN_VERSION_RET = POINTER(struct_tagNET_DVR_RECOMMEN_VERSION_RET)
tagNET_DVR_RECOMMEN_VERSION_RET = struct_tagNET_DVR_RECOMMEN_VERSION_RET
