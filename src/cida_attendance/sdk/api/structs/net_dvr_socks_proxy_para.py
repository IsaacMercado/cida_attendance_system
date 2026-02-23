from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SOCKS_PROXY_PARA(Structure):
    pass

_S(struct_tagNET_DVR_SOCKS_PROXY_PARA, [
    ('byIP', BYTE * 129),
    ('byAuthType', BYTE),
    ('wPort', WORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_SOCKS_PROXY_PARA = struct_tagNET_DVR_SOCKS_PROXY_PARA
LPNET_DVR_SOCKS_PROXY_PARA = POINTER(struct_tagNET_DVR_SOCKS_PROXY_PARA)
tagNET_DVR_SOCKS_PROXY_PARA = struct_tagNET_DVR_SOCKS_PROXY_PARA
