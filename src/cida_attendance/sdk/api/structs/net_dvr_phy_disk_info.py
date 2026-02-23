from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PHY_DISK_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PHY_DISK_INFO, [
    ('wPhySlot', WORD),
    ('byType', BYTE),
    ('byStatus', BYTE),
    ('byMode', BYTE * 40),
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('byArrrayName', BYTE * 16),
    ('wArrayID', WORD),
    ('byArrayInformation', BYTE),
    ('byRes', BYTE * 101),
])

NET_DVR_PHY_DISK_INFO = struct_tagNET_DVR_PHY_DISK_INFO
LPNET_DVR_PHY_DISK_INFO = POINTER(struct_tagNET_DVR_PHY_DISK_INFO)
tagNET_DVR_PHY_DISK_INFO = struct_tagNET_DVR_PHY_DISK_INFO
