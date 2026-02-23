from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_SEARCH_INFO_COND(Structure):
    pass

_S(struct_tagNET_DVR_SEARCH_INFO_COND, [
    ('dwSize', DWORD),
    ('byCommand', BYTE),
    ('byRes1', BYTE * 3),
    ('dwEmployeeNo', DWORD),
    ('byName', BYTE * 32),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byRes', BYTE * 128),
])

NET_DVR_SEARCH_INFO_COND = struct_tagNET_DVR_SEARCH_INFO_COND
LPNET_DVR_SEARCH_INFO_COND = POINTER(struct_tagNET_DVR_SEARCH_INFO_COND)
tagNET_DVR_SEARCH_INFO_COND = struct_tagNET_DVR_SEARCH_INFO_COND
