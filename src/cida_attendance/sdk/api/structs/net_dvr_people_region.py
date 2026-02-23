from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_PEOPLE_REGION(Structure):
    pass

_S(struct_tagNET_DVR_PEOPLE_REGION, [
    ('byID', BYTE),
    ('byNumber', BYTE),
    ('byDressType', BYTE),
    ('byRes', BYTE),
    ('struRegion', NET_VCA_RECT),
    ('dwPicLen', DWORD),
    ('pPicBuffer', String),
    ('byRes1', BYTE * 24),
])

NET_DVR_PEOPLE_REGION = struct_tagNET_DVR_PEOPLE_REGION
LPNET_DVR_PEOPLE_REGION = POINTER(struct_tagNET_DVR_PEOPLE_REGION)
tagNET_DVR_PEOPLE_REGION = struct_tagNET_DVR_PEOPLE_REGION
