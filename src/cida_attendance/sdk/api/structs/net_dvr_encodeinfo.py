from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ENCODEINFO(Structure):
    pass

_S(struct_tagNET_DVR_ENCODEINFO, [
    ('byFormatType', BYTE),
    ('byVideoEncType', BYTE),
    ('wWidth', WORD),
    ('wHeight', WORD),
    ('byRes1', BYTE * 2),
    ('dwVideoBitrate', DWORD),
    ('dwVideoFrameRate', DWORD),
    ('byAudioEncType', BYTE),
    ('byRes2', BYTE * 15),
])

NET_DVR_ENCODEINFO = struct_tagNET_DVR_ENCODEINFO
LPNET_DVR_ENCODEINFO = POINTER(struct_tagNET_DVR_ENCODEINFO)
tagNET_DVR_ENCODEINFO = struct_tagNET_DVR_ENCODEINFO
