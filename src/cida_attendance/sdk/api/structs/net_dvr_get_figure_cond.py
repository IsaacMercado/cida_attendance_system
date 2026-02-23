from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_GET_FIGURE_COND(Structure):
    pass

_S(struct_tagNET_DVR_GET_FIGURE_COND, [
    ('dwLength', DWORD),
    ('dwChannel', DWORD),
    ('struTimePoint', NET_DVR_TIME_V30),
    ('byID', BYTE * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_GET_FIGURE_COND = struct_tagNET_DVR_GET_FIGURE_COND
LPNET_DVR_GET_FIGURE_COND = POINTER(struct_tagNET_DVR_GET_FIGURE_COND)
tagNET_DVR_GET_FIGURE_COND = struct_tagNET_DVR_GET_FIGURE_COND
