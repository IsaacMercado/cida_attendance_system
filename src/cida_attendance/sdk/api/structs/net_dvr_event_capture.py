from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_dvr_rel_capture_chan import NET_DVR_REL_CAPTURE_CHAN


class struct_tagNET_DVR_EVENT_CAPTURE(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_CAPTURE, [
    ('struJpegPara', NET_DVR_JPEGPARA),
    ('dwPicInterval', DWORD),
    ('struRelCaptureChan', NET_DVR_REL_CAPTURE_CHAN * 32),
    ('struAlarmInCapture', NET_DVR_REL_CAPTURE_CHAN * 16),
    ('byCapTimes', BYTE),
    ('byRes', BYTE * 59),
])

NET_DVR_EVENT_CAPTURE = struct_tagNET_DVR_EVENT_CAPTURE
LPNET_DVR_EVENT_CAPTURE = POINTER(struct_tagNET_DVR_EVENT_CAPTURE)
tagNET_DVR_EVENT_CAPTURE = struct_tagNET_DVR_EVENT_CAPTURE
