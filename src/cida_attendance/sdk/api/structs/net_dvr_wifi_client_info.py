from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_WIFI_CLIENT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_WIFI_CLIENT_INFO, [
    ('dwSize', DWORD),
    ('struAddress', NET_DVR_IPADDR),
    ('byMACAddr', BYTE * 6),
    ('wConnSpeed', WORD),
    ('byRSSIValue', BYTE),
    ('byRes1', BYTE),
    ('wBandwidth', WORD),
    ('byRes', BYTE * 32),
])

NET_DVR_WIFI_CLIENT_INFO = struct_tagNET_DVR_WIFI_CLIENT_INFO
LPNET_DVR_WIFI_CLIENT_INFO = POINTER(struct_tagNET_DVR_WIFI_CLIENT_INFO)
tagNET_DVR_WIFI_CLIENT_INFO = struct_tagNET_DVR_WIFI_CLIENT_INFO
