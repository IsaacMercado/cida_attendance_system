from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_response_param import NET_DVR_SCREEN_RESPONSE_PARAM


class struct_tagNET_DVR_SCREEN_RESPONSE_CMD(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_RESPONSE_CMD, [
    ('dwSize', DWORD),
    ('byResponseCmd', BYTE),
    ('byRes1', BYTE * 3),
    ('struResonseParam', NET_DVR_SCREEN_RESPONSE_PARAM),
    ('byRes2', BYTE * 16),
])

NET_DVR_SCREEN_RESPONSE_CMD = struct_tagNET_DVR_SCREEN_RESPONSE_CMD
LPNET_DVR_SCREEN_RESPONSE_CMD = POINTER(struct_tagNET_DVR_SCREEN_RESPONSE_CMD)
tagNET_DVR_SCREEN_RESPONSE_CMD = struct_tagNET_DVR_SCREEN_RESPONSE_CMD
