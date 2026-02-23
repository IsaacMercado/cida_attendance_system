from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_blocklist_info_alarm_log import NET_VCA_BLOCKLIST_INFO_ALARM_LOG
from .net_vca_facesnap_info_alarm_log import NET_VCA_FACESNAP_INFO_ALARM_LOG


class struct_tagNET_VCA_FACESNAP_MATCH_ALARM_LOG(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAP_MATCH_ALARM_LOG, [
    ('dwSize', DWORD),
    ('fSimilarity', c_float),
    ('struSnapInfoLog', NET_VCA_FACESNAP_INFO_ALARM_LOG),
    ('struBlockListInfoLog', NET_VCA_BLOCKLIST_INFO_ALARM_LOG),
    ('byRes', BYTE * 60),
])

NET_VCA_FACESNAP_MATCH_ALARM_LOG = struct_tagNET_VCA_FACESNAP_MATCH_ALARM_LOG
LPNET_VCA_FACESNAP_MATCH_ALARM_LOG = POINTER(struct_tagNET_VCA_FACESNAP_MATCH_ALARM_LOG)
tagNET_VCA_FACESNAP_MATCH_ALARM_LOG = struct_tagNET_VCA_FACESNAP_MATCH_ALARM_LOG
