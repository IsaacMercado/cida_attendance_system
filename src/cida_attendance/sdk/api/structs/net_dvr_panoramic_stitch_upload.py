from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PANORAMIC_STITCH_UPLOAD(Structure):
    pass

_S(struct_tagNET_DVR_PANORAMIC_STITCH_UPLOAD, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_PANORAMIC_STITCH_UPLOAD = struct_tagNET_DVR_PANORAMIC_STITCH_UPLOAD
LPNET_DVR_PANORAMIC_STITCH_UPLOAD = POINTER(struct_tagNET_DVR_PANORAMIC_STITCH_UPLOAD)
tagNET_DVR_PANORAMIC_STITCH_UPLOAD = struct_tagNET_DVR_PANORAMIC_STITCH_UPLOAD
