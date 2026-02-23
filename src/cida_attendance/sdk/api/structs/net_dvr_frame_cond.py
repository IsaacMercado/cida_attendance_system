from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FRAME_COND(Structure):
    pass

_S(struct_tagNET_DVR_FRAME_COND, [
    ('dwSize', DWORD),
    ('dwPicNo', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_FRAME_COND = struct_tagNET_DVR_FRAME_COND
LPNET_DVR_FRAME_COND = POINTER(struct_tagNET_DVR_FRAME_COND)
tagNET_DVR_FRAME_COND = struct_tagNET_DVR_FRAME_COND
