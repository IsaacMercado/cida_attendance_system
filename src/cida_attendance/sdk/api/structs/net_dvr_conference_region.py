from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_point import NET_DVR_POINT


class struct_tagNET_DVR_CONFERENCE_REGION(Structure):
    pass

_S(struct_tagNET_DVR_CONFERENCE_REGION, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('struRegion', NET_DVR_POINT * 4),
    ('dwOutputWidth', DWORD),
    ('dwOutputHeight', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_CONFERENCE_REGION = struct_tagNET_DVR_CONFERENCE_REGION
LPNET_DVR_CONFERENCE_REGION = POINTER(struct_tagNET_DVR_CONFERENCE_REGION)
tagNET_DVR_CONFERENCE_REGION = struct_tagNET_DVR_CONFERENCE_REGION
