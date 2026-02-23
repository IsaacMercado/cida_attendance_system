from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_adapter_version import NET_DVR_ADAPTER_VERSION


class struct_tagNET_DVR_RAID_ADAPTER_INFO(Structure):
    pass

_S(struct_tagNET_DVR_RAID_ADAPTER_INFO, [
    ('dwSize', DWORD),
    ('struVersion', NET_DVR_ADAPTER_VERSION),
    ('bySlotCount', BYTE),
    ('bySupportMigrate', BYTE),
    ('bySupportExpand', BYTE),
    ('bySupportRebuild', BYTE),
    ('wSlotSupportType', WORD),
    ('wSupportRaidType', WORD),
    ('byAutoRebuild', BYTE),
    ('byRes', BYTE * 27),
])

NET_DVR_RAID_ADAPTER_INFO = struct_tagNET_DVR_RAID_ADAPTER_INFO
LPNET_DVR_RAID_ADAPTER_INFO = POINTER(struct_tagNET_DVR_RAID_ADAPTER_INFO)
tagNET_DVR_RAID_ADAPTER_INFO = struct_tagNET_DVR_RAID_ADAPTER_INFO
