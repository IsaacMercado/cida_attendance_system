from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RATIOSTITCHING_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_RATIOSTITCHING_PARAM, [
    ('dwSize', DWORD),
    ('dwFileLen', DWORD),
    ('byChannel', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_RATIOSTITCHING_PARAM = struct_tagNET_DVR_RATIOSTITCHING_PARAM
LPNET_DVR_RATIOSTITCHING_PARAM = POINTER(struct_tagNET_DVR_RATIOSTITCHING_PARAM)
tagNET_DVR_RATIOSTITCHING_PARAM = struct_tagNET_DVR_RATIOSTITCHING_PARAM
