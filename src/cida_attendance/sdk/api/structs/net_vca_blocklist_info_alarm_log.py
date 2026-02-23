from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_blocklist_info import NET_VCA_BLOCKLIST_INFO


class struct_tagNET_VCA_BLOCKLIST_INFO_ALARM_LOG(Structure):
    pass

_S(struct_tagNET_VCA_BLOCKLIST_INFO_ALARM_LOG, [
    ('struBlockListInfo', NET_VCA_BLOCKLIST_INFO),
    ('dwBlockListPicID', DWORD),
    ('byRes', BYTE * 20),
])

NET_VCA_BLOCKLIST_INFO_ALARM_LOG = struct_tagNET_VCA_BLOCKLIST_INFO_ALARM_LOG
LPNET_VCA_BLOCKLIST_INFO_ALARM_LOG = POINTER(struct_tagNET_VCA_BLOCKLIST_INFO_ALARM_LOG)
tagNET_VCA_BLOCKLIST_INFO_ALARM_LOG = struct_tagNET_VCA_BLOCKLIST_INFO_ALARM_LOG
