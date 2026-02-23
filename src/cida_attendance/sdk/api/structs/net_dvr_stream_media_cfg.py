from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_STREAM_MEDIA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_MEDIA_CFG, [
    ('dwSize', DWORD),
    ('sUrl', BYTE * 512),
    ('struDMSIP', NET_DVR_IPADDR),
    ('wDMSPort', WORD),
    ('byRes1', BYTE * 2),
    ('dwDomainID', DWORD),
    ('byRes', BYTE * 360),
])

NET_DVR_STREAM_MEDIA_CFG = struct_tagNET_DVR_STREAM_MEDIA_CFG
LPNET_DVR_STREAM_MEDIA_CFG = POINTER(struct_tagNET_DVR_STREAM_MEDIA_CFG)
tagNET_DVR_STREAM_MEDIA_CFG = struct_tagNET_DVR_STREAM_MEDIA_CFG
