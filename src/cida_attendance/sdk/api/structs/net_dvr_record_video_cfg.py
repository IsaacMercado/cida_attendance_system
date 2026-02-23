from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORD_VIDEO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_VIDEO_CFG, [
    ('dwSize', DWORD),
    ('byExportType', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_RECORD_VIDEO_CFG = struct_tagNET_DVR_RECORD_VIDEO_CFG
LPNET_DVR_RECORD_VIDEO_CFG = POINTER(struct_tagNET_DVR_RECORD_VIDEO_CFG)
tagNET_DVR_RECORD_VIDEO_CFG = struct_tagNET_DVR_RECORD_VIDEO_CFG
