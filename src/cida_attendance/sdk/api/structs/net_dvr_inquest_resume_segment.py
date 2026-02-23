from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_INQUEST_RESUME_SEGMENT(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_RESUME_SEGMENT, [
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byRoomIndex', BYTE),
    ('byDriveIndex', BYTE),
    ('wSegmetSize', WORD),
    ('dwSegmentNo', DWORD),
    ('byRes', BYTE * 24),
])

NET_DVR_INQUEST_RESUME_SEGMENT = struct_tagNET_DVR_INQUEST_RESUME_SEGMENT
LPNET_DVR_INQUEST_RESUME_SEGMENT = POINTER(struct_tagNET_DVR_INQUEST_RESUME_SEGMENT)
tagNET_DVR_INQUEST_RESUME_SEGMENT = struct_tagNET_DVR_INQUEST_RESUME_SEGMENT
