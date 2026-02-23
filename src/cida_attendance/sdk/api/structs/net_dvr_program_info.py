from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PROGRAM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PROGRAM_INFO, [
    ('dwProgramNo', DWORD),
    ('sProgramName', BYTE * 32),
    ('byRes', BYTE * 16),
])

NET_DVR_PROGRAM_INFO = struct_tagNET_DVR_PROGRAM_INFO
LPNET_DVR_PROGRAM_INFO = POINTER(struct_tagNET_DVR_PROGRAM_INFO)
tagNET_DVR_PROGRAM_INFO = struct_tagNET_DVR_PROGRAM_INFO
