from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_dvr_rel_capture_chan_v40 import NET_DVR_REL_CAPTURE_CHAN_V40


class struct_tagNET_DVR_EVENT_CAPTURE_V40(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_CAPTURE_V40, [
    ('struJpegPara', NET_DVR_JPEGPARA),
    ('dwPicInterval', DWORD),
    ('struRelCaptureChan', NET_DVR_REL_CAPTURE_CHAN_V40 * 32),
    ('struAlarmInCapture', NET_DVR_REL_CAPTURE_CHAN_V40 * 16),
    ('dwMaxGroupNum', DWORD),
    ('byCapTimes', BYTE),
    ('byRes', BYTE * 59),
])

NET_DVR_EVENT_CAPTURE_V40 = struct_tagNET_DVR_EVENT_CAPTURE_V40
LPNET_DVR_EVENT_CAPTURE_V40 = POINTER(struct_tagNET_DVR_EVENT_CAPTURE_V40)
tagNET_DVR_EVENT_CAPTURE_V40 = struct_tagNET_DVR_EVENT_CAPTURE_V40
