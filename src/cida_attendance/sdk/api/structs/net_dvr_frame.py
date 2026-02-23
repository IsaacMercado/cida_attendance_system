from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_NET_DVR_FRAME(Structure):
    pass

_S(struct_NET_DVR_FRAME, [
    ('byFrameWide', BYTE),
    ('byRed', BYTE),
    ('byGreen', BYTE),
    ('byBlue', BYTE),
    ('byRes', BYTE * 256),
])

NET_DVR_FRAME = struct_NET_DVR_FRAME
LPNET_DVR_FRAME = POINTER(struct_NET_DVR_FRAME)
NET_DVR_FRAME = struct_NET_DVR_FRAME
