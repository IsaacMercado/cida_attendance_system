from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_206 import NET_DVR_POINT_FRAME


class struct_tagNET_DVR_WIN_ZOOM_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_WIN_ZOOM_STATUS, [
    ('dwSize', DWORD),
    ('byZoomStatus', BYTE),
    ('byRes1', BYTE * 3),
    ('struPointFrame', NET_DVR_POINT_FRAME),
    ('byRes2', BYTE * 32),
])

NET_DVR_WIN_ZOOM_STATUS = struct_tagNET_DVR_WIN_ZOOM_STATUS
LPNET_DVR_WIN_ZOOM_STATUS = POINTER(struct_tagNET_DVR_WIN_ZOOM_STATUS)
tagNET_DVR_WIN_ZOOM_STATUS = struct_tagNET_DVR_WIN_ZOOM_STATUS
