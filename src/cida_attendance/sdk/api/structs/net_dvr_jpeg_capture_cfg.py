from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_event_capture import NET_DVR_EVENT_CAPTURE
from .net_dvr_timing_capture import NET_DVR_TIMING_CAPTURE


class struct_tagNET_DVR_JPEG_CAPTURE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_JPEG_CAPTURE_CFG, [
    ('dwSize', DWORD),
    ('struTimingCapture', NET_DVR_TIMING_CAPTURE),
    ('struEventCapture', NET_DVR_EVENT_CAPTURE),
    ('byStreamType', BYTE),
    ('byRes3', BYTE * 19),
])

NET_DVR_JPEG_CAPTURE_CFG = struct_tagNET_DVR_JPEG_CAPTURE_CFG
LPNET_DVR_JPEG_CAPTURE_CFG = POINTER(struct_tagNET_DVR_JPEG_CAPTURE_CFG)
tagNET_DVR_JPEG_CAPTURE_CFG = struct_tagNET_DVR_JPEG_CAPTURE_CFG
