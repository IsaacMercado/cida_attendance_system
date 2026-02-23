from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RAID_BTS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RAID_BTS_CFG, [
    ('dwSize', DWORD),
    ('bySpeed', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_RAID_BTS_CFG = struct_tagNET_DVR_RAID_BTS_CFG
LPNET_DVR_RAID_BTS_CFG = POINTER(struct_tagNET_DVR_RAID_BTS_CFG)
tagNET_DVR_RAID_BTS_CFG = struct_tagNET_DVR_RAID_BTS_CFG
