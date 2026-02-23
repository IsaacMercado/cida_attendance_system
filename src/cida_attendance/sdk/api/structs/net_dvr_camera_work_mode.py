from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAMERA_WORK_MODE(Structure):
    pass

_S(struct_tagNET_DVR_CAMERA_WORK_MODE, [
    ('dwSize', DWORD),
    ('byWorkMode', BYTE),
    ('byPreviewImageMode', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_CAMERA_WORK_MODE = struct_tagNET_DVR_CAMERA_WORK_MODE
LPNET_DVR_CAMERA_WORK_MODE = POINTER(struct_tagNET_DVR_CAMERA_WORK_MODE)
tagNET_DVR_CAMERA_WORK_MODE = struct_tagNET_DVR_CAMERA_WORK_MODE
