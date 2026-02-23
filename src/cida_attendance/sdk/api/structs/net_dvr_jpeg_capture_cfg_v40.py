from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_event_capture_v40 import NET_DVR_EVENT_CAPTURE_V40
from .net_dvr_timing_capture import NET_DVR_TIMING_CAPTURE


class struct_tagNET_DVR_JPEG_CAPTURE_CFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_JPEG_CAPTURE_CFG_V40, [
    ('dwSize', DWORD),
    ('struTimingCapture', NET_DVR_TIMING_CAPTURE),
    ('struEventCapture', NET_DVR_EVENT_CAPTURE_V40),
    ('byStreamType', BYTE),
    ('byRes3', BYTE * 19),
])

NET_DVR_JPEG_CAPTURE_CFG_V40 = struct_tagNET_DVR_JPEG_CAPTURE_CFG_V40
LPNET_DVR_JPEG_CAPTURE_CFG_V40 = POINTER(struct_tagNET_DVR_JPEG_CAPTURE_CFG_V40)
tagNET_DVR_JPEG_CAPTURE_CFG_V40 = struct_tagNET_DVR_JPEG_CAPTURE_CFG_V40
