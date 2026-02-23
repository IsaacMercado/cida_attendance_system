from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_bga_info import NET_DVR_BGA_INFO


class struct_tagNET_DVR_ARRAY_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ARRAY_INFO, [
    ('wArrayID', WORD),
    ('byRaidMode', BYTE),
    ('byStatus', BYTE),
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('dwHFreeSpace', DWORD),
    ('dwLFreeSpace', DWORD),
    ('byArrayName', BYTE * 16),
    ('byPDCount', BYTE),
    ('bySpareCount', BYTE),
    ('byRes1', BYTE * 2),
    ('wPDSlots', WORD * 16),
    ('wSparePDSlots', WORD * 16),
    ('struBgaInfo', NET_DVR_BGA_INFO),
    ('wPDSlotsPartTwo', WORD * 8),
    ('wSparePDSlotsPartTwo', WORD * 8),
    ('byRes2', BYTE * 48),
])

NET_DVR_ARRAY_INFO = struct_tagNET_DVR_ARRAY_INFO
LPNET_DVR_ARRAY_INFO = POINTER(struct_tagNET_DVR_ARRAY_INFO)
tagNET_DVR_ARRAY_INFO = struct_tagNET_DVR_ARRAY_INFO
