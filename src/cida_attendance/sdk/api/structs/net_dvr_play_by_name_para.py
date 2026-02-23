from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, HWND
from ..ctypes_preamble import POINTER
from .net_dvr_address import NET_DVR_ADDRESS


class struct_tagNET_DVR_PLAY_BY_NAME_PARA(Structure):
    pass

_S(struct_tagNET_DVR_PLAY_BY_NAME_PARA, [
    ('szFileName', c_char * 100),
    ('byDownload', BYTE),
    ('byRes1', BYTE * 127),
    ('hWnd', HWND),
    ('struAddr', NET_DVR_ADDRESS),
    ('byRes2', BYTE * 256),
])

NET_DVR_PLAY_BY_NAME_PARA = struct_tagNET_DVR_PLAY_BY_NAME_PARA
LPNET_DVR_PLAY_BY_NAME_PARA = POINTER(struct_tagNET_DVR_PLAY_BY_NAME_PARA)
tagNET_DVR_PLAY_BY_NAME_PARA = struct_tagNET_DVR_PLAY_BY_NAME_PARA
