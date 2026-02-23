from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAM_ATTACHINFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_ATTACHINFO_CFG, [
    ('dwSize', DWORD),
    ('byStreamWithVca', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_STREAM_ATTACHINFO_CFG = struct_tagNET_DVR_STREAM_ATTACHINFO_CFG
LPNET_DVR_STREAM_ATTACHINFO_CFG = POINTER(struct_tagNET_DVR_STREAM_ATTACHINFO_CFG)
tagNET_DVR_STREAM_ATTACHINFO_CFG = struct_tagNET_DVR_STREAM_ATTACHINFO_CFG
