from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_inquest_resume_segment import NET_DVR_INQUEST_RESUME_SEGMENT


class struct_tagNET_DVR_INQUEST_RESUME_EVENT(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_RESUME_EVENT, [
    ('dwResumeNum', DWORD),
    ('struResumeSegment', NET_DVR_INQUEST_RESUME_SEGMENT * 2),
    ('byResumeMode', BYTE),
    ('byCDPrintEnbled', BYTE),
    ('byRes', BYTE * 198),
])

NET_DVR_INQUEST_RESUME_EVENT = struct_tagNET_DVR_INQUEST_RESUME_EVENT
LPNET_DVR_INQUEST_RESUME_EVENT = POINTER(struct_tagNET_DVR_INQUEST_RESUME_EVENT)
tagNET_DVR_INQUEST_RESUME_EVENT = struct_tagNET_DVR_INQUEST_RESUME_EVENT
