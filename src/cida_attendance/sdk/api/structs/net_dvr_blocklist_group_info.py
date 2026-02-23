from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BLOCKLIST_GROUP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_GROUP_INFO, [
    ('dwSize', DWORD),
    ('dwGroupID', DWORD),
    ('dwGroupNo', DWORD),
    ('byGroupType', BYTE),
    ('byRes1', BYTE),
    ('wThreshold', WORD),
    ('dwListNum', DWORD),
    ('szGroupName', BYTE * 32),
    ('szRemark', BYTE * 256),
    ('byStorageAddr', BYTE * 64),
    ('wStoragePort', WORD),
    ('byRes', BYTE * 126),
])

NET_DVR_BLOCKLIST_GROUP_INFO = struct_tagNET_DVR_BLOCKLIST_GROUP_INFO
LPNET_DVR_BLOCKLIST_GROUP_INFO = POINTER(struct_tagNET_DVR_BLOCKLIST_GROUP_INFO)
tagNET_DVR_BLOCKLIST_GROUP_INFO = struct_tagNET_DVR_BLOCKLIST_GROUP_INFO
