from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUBLISH_PROGRESS_COND(Structure):
    pass

_S(struct_tagNET_DVR_PUBLISH_PROGRESS_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byFileID', BYTE * 128),
    ('byRes', BYTE * 256),
])

NET_DVR_PUBLISH_PROGRESS_COND = struct_tagNET_DVR_PUBLISH_PROGRESS_COND
LPNET_DVR_PUBLISH_PROGRESS_COND = POINTER(struct_tagNET_DVR_PUBLISH_PROGRESS_COND)
tagNET_DVR_PUBLISH_PROGRESS_COND = struct_tagNET_DVR_PUBLISH_PROGRESS_COND
