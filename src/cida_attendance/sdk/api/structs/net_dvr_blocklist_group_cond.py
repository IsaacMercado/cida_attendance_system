from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BLOCKLIST_GROUP_COND(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_GROUP_COND, [
    ('dwSize', DWORD),
    ('dwGroupID', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_BLOCKLIST_GROUP_COND = struct_tagNET_DVR_BLOCKLIST_GROUP_COND
LPNET_DVR_BLOCKLIST_GROUP_COND = POINTER(struct_tagNET_DVR_BLOCKLIST_GROUP_COND)
tagNET_DVR_BLOCKLIST_GROUP_COND = struct_tagNET_DVR_BLOCKLIST_GROUP_COND
