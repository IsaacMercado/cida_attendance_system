from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_33(Structure):
    pass

_S(struct_anon_33, [
    ('byStreamType', BYTE),
    ('byResolution', BYTE),
    ('byBitrateType', BYTE),
    ('byPicQuality', BYTE),
    ('dwVideoBitrate', DWORD),
    ('dwVideoFrameRate', DWORD),
])

NET_DVR_COMPRESSION_INFO = struct_anon_33
LPNET_DVR_COMPRESSION_INFO = POINTER(struct_anon_33)
