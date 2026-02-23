from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_blocklist_group_record import NET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD


class struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_CFG, [
    ('dwSize', DWORD),
    ('dwRecordNum', DWORD),
    ('struRecord', NET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD * 10),
    ('byRes', BYTE * 256),
])

NET_DVR_BLOCKLIST_GROUP_RECORD_CFG = struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_CFG
LPNET_DVR_BLOCKLIST_GROUP_RECORD_CFG = POINTER(struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_CFG)
tagNET_DVR_BLOCKLIST_GROUP_RECORD_CFG = struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_CFG
