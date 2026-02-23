from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PIC_VIEW_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PIC_VIEW_PARAM, [
    ('dwSize', DWORD),
    ('struCuIp', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('bySourceIndex', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_PIC_VIEW_PARAM = struct_tagNET_DVR_PIC_VIEW_PARAM
LPNET_DVR_PIC_VIEW_PARAM = POINTER(struct_tagNET_DVR_PIC_VIEW_PARAM)
tagNET_DVR_PIC_VIEW_PARAM = struct_tagNET_DVR_PIC_VIEW_PARAM
