from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG, [
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('struDevIP', NET_DVR_IPADDR),
    ('wDevPort', WORD),
    ('byTransmitType', BYTE),
    ('byRes2', BYTE * 69),
])

NET_DVR_STREAM_MEDIA_SERVER_CFG = struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG
LPNET_DVR_STREAM_MEDIA_SERVER_CFG = POINTER(struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG)
tagNET_DVR_STREAM_MEDIA_SERVER_CFG = struct_tagNET_DVR_STREAM_MEDIA_SERVER_CFG
