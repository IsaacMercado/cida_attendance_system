from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_CAPTURE_SCHED(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_SCHED, [
    ('struCaptureTime', NET_DVR_SCHEDTIME),
    ('byCaptureType', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_CAPTURE_SCHED = struct_tagNET_DVR_CAPTURE_SCHED
LPNET_DVR_CAPTURE_SCHED = POINTER(struct_tagNET_DVR_CAPTURE_SCHED)
tagNET_DVR_CAPTURE_SCHED = struct_tagNET_DVR_CAPTURE_SCHED
