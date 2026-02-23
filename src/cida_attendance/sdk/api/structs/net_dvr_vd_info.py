from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_bga_info import NET_DVR_BGA_INFO


class struct_tagNET_DVR_VD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VD_INFO, [
    ('wSlot', WORD),
    ('byStatus', BYTE),
    ('byRaidMode', BYTE),
    ('wArrayID', WORD),
    ('byRepair', BYTE),
    ('byUsage', BYTE),
    ('byArrayName', BYTE * 16),
    ('byName', BYTE * 16),
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('dwHFreeSpace', DWORD),
    ('dwLFreeSpace', DWORD),
    ('struBgaInfo', NET_DVR_BGA_INFO),
    ('dwBlockSize', DWORD),
    ('struWarrantIP', NET_DVR_IPADDR),
    ('szArrayGroup', c_char * 32),
    ('byRes', BYTE * 20),
])

NET_DVR_VD_INFO = struct_tagNET_DVR_VD_INFO
LPNET_DVR_VD_INFO = POINTER(struct_tagNET_DVR_VD_INFO)
tagNET_DVR_VD_INFO = struct_tagNET_DVR_VD_INFO
