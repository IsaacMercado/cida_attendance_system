from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_CONFERENCE_CALL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CONFERENCE_CALL_INFO, [
    ('byConferenceID', BYTE * 48),
    ('byConferenceName', BYTE * 32),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byRes', BYTE * 512),
])

NET_DVR_CONFERENCE_CALL_INFO = struct_tagNET_DVR_CONFERENCE_CALL_INFO
LPNET_DVR_CONFERENCE_CALL_INFO = POINTER(struct_tagNET_DVR_CONFERENCE_CALL_INFO)
tagNET_DVR_CONFERENCE_CALL_INFO = struct_tagNET_DVR_CONFERENCE_CALL_INFO
