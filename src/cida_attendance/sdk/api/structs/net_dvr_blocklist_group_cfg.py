from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_blocklist_group_info import NET_DVR_BLOCKLIST_GROUP_INFO


class struct_tagNET_DVR_BLOCKLIST_GROUP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_GROUP_CFG, [
    ('dwSize', DWORD),
    ('dwGroupNum', DWORD),
    ('struGroup', NET_DVR_BLOCKLIST_GROUP_INFO * 10),
    ('byRes', BYTE * 256),
])

NET_DVR_BLOCKLIST_GROUP_CFG = struct_tagNET_DVR_BLOCKLIST_GROUP_CFG
LPNET_DVR_BLOCKLIST_GROUP_CFG = POINTER(struct_tagNET_DVR_BLOCKLIST_GROUP_CFG)
tagNET_DVR_BLOCKLIST_GROUP_CFG = struct_tagNET_DVR_BLOCKLIST_GROUP_CFG
