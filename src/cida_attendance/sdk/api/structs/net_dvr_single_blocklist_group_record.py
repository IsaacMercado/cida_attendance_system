from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_addr_domain_info import NET_DVR_ADDR_DOMAIN_INFO


class struct_tagNET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD, [
    ('dwSize', DWORD),
    ('dwGroupRecordID', DWORD),
    ('dwGroupNo', DWORD),
    ('dwFaceDBID', DWORD),
    ('dwFaceRecordID', DWORD),
    ('byAlarmLevel', BYTE),
    ('byRes1', BYTE * 3),
    ('struStorageAddr', NET_DVR_ADDR_DOMAIN_INFO),
    ('byRes', BYTE * 256),
])

NET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD = struct_tagNET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD
LPNET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD = POINTER(struct_tagNET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD)
tagNET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD = struct_tagNET_DVR_SINGLE_BLOCKLIST_GROUP_RECORD
