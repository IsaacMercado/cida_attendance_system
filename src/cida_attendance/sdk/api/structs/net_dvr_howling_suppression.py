from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HOWLING_SUPPRESSION(Structure):
    pass

_S(struct_tagNET_DVR_HOWLING_SUPPRESSION, [
    ('byEnabled', BYTE),
    ('byHsSensibility', BYTE),
    ('byHsMode', BYTE),
    ('byRes1', BYTE),
    ('dwHsTime', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_HOWLING_SUPPRESSION = struct_tagNET_DVR_HOWLING_SUPPRESSION
LPNET_DVR_HOWLING_SUPPRESSION = POINTER(struct_tagNET_DVR_HOWLING_SUPPRESSION)
tagNET_DVR_HOWLING_SUPPRESSION = struct_tagNET_DVR_HOWLING_SUPPRESSION
