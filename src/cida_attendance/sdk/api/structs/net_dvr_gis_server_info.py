from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_GIS_SERVER_INFO(Structure):
    pass

_S(struct_tagNET_DVR_GIS_SERVER_INFO, [
    ('byUserName', BYTE * 32),
    ('byPassword', BYTE * 16),
    ('struServerIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_GIS_SERVER_INFO = struct_tagNET_DVR_GIS_SERVER_INFO
LPNET_DVR_GIS_SERVER_INFO = POINTER(struct_tagNET_DVR_GIS_SERVER_INFO)
tagNET_DVR_GIS_SERVER_INFO = struct_tagNET_DVR_GIS_SERVER_INFO
