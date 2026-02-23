from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZPOS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PTZPOS_INFO, [
    ('dwPanPos', DWORD),
    ('dwTiltPos', DWORD),
    ('dwZoomPos', DWORD),
])

NET_DVR_PTZPOS_INFO = struct_tagNET_DVR_PTZPOS_INFO
LPNET_DVR_PTZPOS_INFO = POINTER(struct_tagNET_DVR_PTZPOS_INFO)
tagNET_DVR_PTZPOS_INFO = struct_tagNET_DVR_PTZPOS_INFO
