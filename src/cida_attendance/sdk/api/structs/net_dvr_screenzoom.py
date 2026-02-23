from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_206 import NET_DVR_POINT_FRAME


class struct_tagNET_DVR_SCREENZOOM(Structure):
    pass

_S(struct_tagNET_DVR_SCREENZOOM, [
    ('dwSize', DWORD),
    ('dwScreenNum', DWORD),
    ('struPointFrame', NET_DVR_POINT_FRAME),
    ('byLayer', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_SCREENZOOM = struct_tagNET_DVR_SCREENZOOM
LPNET_DVR_SCREENZOOM = POINTER(struct_tagNET_DVR_SCREENZOOM)
tagNET_DVR_SCREENZOOM = struct_tagNET_DVR_SCREENZOOM
