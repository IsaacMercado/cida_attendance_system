from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECOMMEN_VERSION_COND(Structure):
    pass

_S(struct_tagNET_DVR_RECOMMEN_VERSION_COND, [
    ('dwSize', DWORD),
    ('byFirmwareCode', BYTE * 128),
    ('byFirmwareVersion', BYTE * 64),
    ('byRes', BYTE * 60),
])

NET_DVR_RECOMMEN_VERSION_COND = struct_tagNET_DVR_RECOMMEN_VERSION_COND
LPNET_DVR_RECOMMEN_VERSION_COND = POINTER(struct_tagNET_DVR_RECOMMEN_VERSION_COND)
tagNET_DVR_RECOMMEN_VERSION_COND = struct_tagNET_DVR_RECOMMEN_VERSION_COND
