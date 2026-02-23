from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_sub_insertplay_progress import LPNET_DVR_SUB_INSERTPLAY_PROGRESS


class struct_tagNET_DVR_INSERTPLAY_PROGRESS_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_INSERTPLAY_PROGRESS_RESULT, [
    ('dwSize', DWORD),
    ('dwMainProgress', DWORD),
    ('dwSubProgressNum', DWORD),
    ('lpStruSubProgress', LPNET_DVR_SUB_INSERTPLAY_PROGRESS),
    ('byRes', BYTE * 32),
])

NET_DVR_INSERTPLAY_PROGRESS_RESULT = struct_tagNET_DVR_INSERTPLAY_PROGRESS_RESULT
LPNET_DVR_INSERTPLAY_PROGRESS_RESULT = POINTER(struct_tagNET_DVR_INSERTPLAY_PROGRESS_RESULT)
tagNET_DVR_INSERTPLAY_PROGRESS_RESULT = struct_tagNET_DVR_INSERTPLAY_PROGRESS_RESULT
