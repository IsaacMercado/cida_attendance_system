from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PANORAMAIMAGE(Structure):
    pass

_S(struct_tagNET_DVR_PANORAMAIMAGE, [
    ('dwSize', DWORD),
    ('byFusionMode', BYTE),
    ('byPreviewMode', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_PANORAMAIMAGE = struct_tagNET_DVR_PANORAMAIMAGE
LPNET_DVR_PANORAMAIMAGE = POINTER(struct_tagNET_DVR_PANORAMAIMAGE)
tagNET_DVR_PANORAMAIMAGE = struct_tagNET_DVR_PANORAMAIMAGE
