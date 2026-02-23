from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FORENSICS_MODE(Structure):
    pass

_S(struct_tagNET_DVR_FORENSICS_MODE, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_FORENSICS_MODE = struct_tagNET_DVR_FORENSICS_MODE
LPNET_DVR_FORENSICS_MODE = POINTER(struct_tagNET_DVR_FORENSICS_MODE)
tagNET_DVR_FORENSICS_MODE = struct_tagNET_DVR_FORENSICS_MODE
