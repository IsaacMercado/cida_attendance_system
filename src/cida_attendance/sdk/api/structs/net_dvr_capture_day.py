from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAPTURE_DAY(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_DAY, [
    ('byAllDayCapture', BYTE),
    ('byCaptureType', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_CAPTURE_DAY = struct_tagNET_DVR_CAPTURE_DAY
LPNET_DVR_CAPTURE_DAY = POINTER(struct_tagNET_DVR_CAPTURE_DAY)
tagNET_DVR_CAPTURE_DAY = struct_tagNET_DVR_CAPTURE_DAY
