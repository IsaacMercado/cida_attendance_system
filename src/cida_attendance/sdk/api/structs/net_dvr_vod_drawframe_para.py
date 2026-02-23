from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_VOD_DRAWFRAME_PARA(Structure):
    pass

_S(struct_tagNET_DVR_VOD_DRAWFRAME_PARA, [
    ('struTime', NET_DVR_TIME_EX),
    ('dwDrawType', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_VOD_DRAWFRAME_PARA = struct_tagNET_DVR_VOD_DRAWFRAME_PARA
LPNET_DVR_VOD_DRAWFRAME_PARA = POINTER(struct_tagNET_DVR_VOD_DRAWFRAME_PARA)
tagNET_DVR_VOD_DRAWFRAME_PARA = struct_tagNET_DVR_VOD_DRAWFRAME_PARA
