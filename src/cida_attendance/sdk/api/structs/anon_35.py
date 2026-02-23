from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_35(Structure):
    pass

_S(struct_anon_35, [
    ('byStreamType', BYTE),
    ('byResolution', BYTE),
    ('byBitrateType', BYTE),
    ('byPicQuality', BYTE),
    ('dwVideoBitrate', DWORD),
    ('dwVideoFrameRate', DWORD),
    ('wIntervalFrameI', WORD),
    ('byIntervalBPFrame', BYTE),
    ('byRes', BYTE),
])

NET_DVR_COMPRESSION_INFO_EX = struct_anon_35
LPNET_DVR_COMPRESSION_INFO_EX = POINTER(struct_anon_35)
