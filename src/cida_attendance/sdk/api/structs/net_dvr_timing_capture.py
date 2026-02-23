from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA


class struct_tagNET_DVR_TIMING_CAPTURE(Structure):
    pass

_S(struct_tagNET_DVR_TIMING_CAPTURE, [
    ('struJpegPara', NET_DVR_JPEGPARA),
    ('dwPicInterval', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_TIMING_CAPTURE = struct_tagNET_DVR_TIMING_CAPTURE
LPNET_DVR_TIMING_CAPTURE = POINTER(struct_tagNET_DVR_TIMING_CAPTURE)
tagNET_DVR_TIMING_CAPTURE = struct_tagNET_DVR_TIMING_CAPTURE
