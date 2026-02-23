from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION, [
    ('dwSize', DWORD),
    ('dwInputSignalNo', DWORD),
    ('byEnabled', BYTE),
    ('byRes', BYTE),
    ('wImageWidth', WORD),
    ('wImageHeight', WORD),
    ('wRefreshRate', WORD),
    ('byColorDepth', BYTE),
    ('byScanType', BYTE),
    ('byRes1', BYTE * 62),
])

NET_DVR_INPUT_SOURCE_RESOLUTION = struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION
LPNET_DVR_INPUT_SOURCE_RESOLUTION = POINTER(struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION)
tagNET_DVR_INPUT_SOURCE_RESOLUTION = struct_tagNET_DVR_INPUT_SOURCE_RESOLUTION
