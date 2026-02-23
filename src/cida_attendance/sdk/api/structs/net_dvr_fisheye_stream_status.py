from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FISHEYE_STREAM_STATUS_(Structure):
    pass

_S(struct_tagNET_DVR_FISHEYE_STREAM_STATUS_, [
    ('dwSize', DWORD),
    ('byStreamMode', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_FISHEYE_STREAM_STATUS = struct_tagNET_DVR_FISHEYE_STREAM_STATUS_
LPNET_DVR_FISHEYE_STREAM_STATUS = POINTER(struct_tagNET_DVR_FISHEYE_STREAM_STATUS_)
tagNET_DVR_FISHEYE_STREAM_STATUS_ = struct_tagNET_DVR_FISHEYE_STREAM_STATUS_
