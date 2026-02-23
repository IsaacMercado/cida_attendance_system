from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_COND(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_COND, [
    ('dwSize', DWORD),
    ('dwRecordID', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_BLOCKLIST_GROUP_RECORD_COND = struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_COND
LPNET_DVR_BLOCKLIST_GROUP_RECORD_COND = POINTER(struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_COND)
tagNET_DVR_BLOCKLIST_GROUP_RECORD_COND = struct_tagNET_DVR_BLOCKLIST_GROUP_RECORD_COND
