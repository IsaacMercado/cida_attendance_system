from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, SHORT, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CALLER_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CALLER_INFO, [
    ('dwSize', DWORD),
    ('wBuildingNo', WORD),
    ('wFloorNo', SHORT),
    ('byZoneNo', BYTE),
    ('byUnitNo', BYTE),
    ('byDevNo', BYTE),
    ('byDevType', BYTE),
    ('byLockNum', BYTE),
    ('byHighDevNo', BYTE),
    ('byRes1', BYTE * 2),
    ('byVoipNo', BYTE * 16),
    ('byRes', BYTE * 80),
])

NET_DVR_CALLER_INFO = struct_tagNET_DVR_CALLER_INFO
LPNET_DVR_CALLER_INFO = POINTER(struct_tagNET_DVR_CALLER_INFO)
tagNET_DVR_CALLER_INFO = struct_tagNET_DVR_CALLER_INFO
