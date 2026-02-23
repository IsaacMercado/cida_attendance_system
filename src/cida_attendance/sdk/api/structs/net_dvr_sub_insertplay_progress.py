from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SUB_INSERTPLAY_PROGRESS(Structure):
    pass

_S(struct_tagNET_DVR_SUB_INSERTPLAY_PROGRESS, [
    ('dwTerminalNo', DWORD),
    ('dwProgress', DWORD),
])

NET_DVR_SUB_INSERTPLAY_PROGRESS = struct_tagNET_DVR_SUB_INSERTPLAY_PROGRESS
LPNET_DVR_SUB_INSERTPLAY_PROGRESS = POINTER(struct_tagNET_DVR_SUB_INSERTPLAY_PROGRESS)
tagNET_DVR_SUB_INSERTPLAY_PROGRESS = struct_tagNET_DVR_SUB_INSERTPLAY_PROGRESS
