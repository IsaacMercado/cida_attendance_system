from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAPTURE_PICTURE_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_PICTURE_RESULT, [
    ('dwSize', DWORD),
    ('dwReturnPicSize', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_CAPTURE_PICTURE_RESULT = struct_tagNET_DVR_CAPTURE_PICTURE_RESULT
LPNET_DVR_CAPTURE_PICTURE_RESULT = POINTER(struct_tagNET_DVR_CAPTURE_PICTURE_RESULT)
tagNET_DVR_CAPTURE_PICTURE_RESULT = struct_tagNET_DVR_CAPTURE_PICTURE_RESULT
