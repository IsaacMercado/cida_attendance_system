from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXDEVDET_COND(Structure):
    pass

_S(struct_tagNET_DVR_EXDEVDET_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byExternalDevType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_EXDEVDET_COND = struct_tagNET_DVR_EXDEVDET_COND
LPNET_DVR_EXDEVDET_COND = POINTER(struct_tagNET_DVR_EXDEVDET_COND)
tagNET_DVR_EXDEVDET_COND = struct_tagNET_DVR_EXDEVDET_COND
