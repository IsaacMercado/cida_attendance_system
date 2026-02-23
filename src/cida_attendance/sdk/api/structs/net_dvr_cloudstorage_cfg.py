from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_poolparam import NET_DVR_POOLPARAM


class struct_tagNET_DVR_CLOUDSTORAGE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CLOUDSTORAGE_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes1', BYTE * 2),
    ('szUser', c_char * 48),
    ('szPassword', c_char * 48),
    ('struPoolInfo', NET_DVR_POOLPARAM * 16),
    ('byRes2', BYTE * 128),
])

NET_DVR_CLOUDSTORAGE_CFG = struct_tagNET_DVR_CLOUDSTORAGE_CFG
LPNET_DVR_CLOUDSTORAGE_CFG = POINTER(struct_tagNET_DVR_CLOUDSTORAGE_CFG)
tagNET_DVR_CLOUDSTORAGE_CFG = struct_tagNET_DVR_CLOUDSTORAGE_CFG
