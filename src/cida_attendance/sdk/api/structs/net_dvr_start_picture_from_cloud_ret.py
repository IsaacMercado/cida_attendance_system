from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_RET(Structure):
    pass

_S(struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_RET, [
    ('dwSize', DWORD),
    ('dwFileCount', DWORD),
    ('byRes', BYTE * 120),
])

NET_DVR_START_PICTURE_FROM_CLOUD_RET = struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_RET
LPNET_DVR_START_PICTURE_FROM_CLOUD_RET = POINTER(struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_RET)
tagNET_DVR_START_PICTURE_FROM_CLOUD_RET = struct_tagNET_DVR_START_PICTURE_FROM_CLOUD_RET
