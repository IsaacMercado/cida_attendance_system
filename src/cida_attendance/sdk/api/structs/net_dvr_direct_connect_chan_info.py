from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO, [
    ('byEnable', BYTE),
    ('byProType', BYTE),
    ('byZeroChan', BYTE),
    ('byPriority', BYTE),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byDomain', BYTE * 64),
    ('struIP', NET_DVR_IPADDR),
    ('wDVRPort', WORD),
    ('byStreamType', BYTE),
    ('byOnline', BYTE),
    ('dwChannel', DWORD),
    ('byTransProtocol', BYTE),
    ('byLocalBackUp', BYTE),
    ('wDirectLastTime', WORD),
    ('byChanNo', BYTE * 24),
])

NET_DVR_DIRECT_CONNECT_CHAN_INFO = struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO
LPNET_DVR_DIRECT_CONNECT_CHAN_INFO = POINTER(struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO)
tagNET_DVR_DIRECT_CONNECT_CHAN_INFO = struct_tagNET_DVR_DIRECT_CONNECT_CHAN_INFO
