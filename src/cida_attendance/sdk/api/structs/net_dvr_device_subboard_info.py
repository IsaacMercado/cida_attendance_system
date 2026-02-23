from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subboard_info import NET_DVR_SUBBOARD_INFO


class struct_tagNET_DVR_DEVICE_SUBBOARD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_SUBBOARD_INFO, [
    ('dwSize', DWORD),
    ('byBackBoardType', BYTE),
    ('bySoltNum', BYTE),
    ('byBoardNum', BYTE),
    ('byRes1', BYTE * 1),
    ('struSubBoadInfo', NET_DVR_SUBBOARD_INFO * 42),
    ('byRes2', BYTE * 32),
])

NET_DVR_DEVICE_SUBBOARD_INFO = struct_tagNET_DVR_DEVICE_SUBBOARD_INFO
LPNET_DVR_DEVICE_SUBBOARD_INFO = POINTER(struct_tagNET_DVR_DEVICE_SUBBOARD_INFO)
tagNET_DVR_DEVICE_SUBBOARD_INFO = struct_tagNET_DVR_DEVICE_SUBBOARD_INFO
