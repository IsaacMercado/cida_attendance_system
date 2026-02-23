from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_blocklist_info_alarm import NET_VCA_BLOCKLIST_INFO_ALARM
from .net_vca_facesnap_info_alarm import NET_VCA_FACESNAP_INFO_ALARM
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_FACESNAP_MATCH_ALARM(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAP_MATCH_ALARM, [
    ('dwSize', DWORD),
    ('fSimilarity', c_float),
    ('struSnapInfo', NET_VCA_FACESNAP_INFO_ALARM),
    ('struBlockListInfo', NET_VCA_BLOCKLIST_INFO_ALARM),
    ('sStorageIP', c_char * 16),
    ('wStoragePort', WORD),
    ('byMatchPicNum', BYTE),
    ('byPicTransType', BYTE),
    ('dwSnapPicLen', DWORD),
    ('pSnapPicBuffer', POINTER(BYTE)),
    ('struRegion', NET_VCA_RECT),
    ('dwModelDataLen', DWORD),
    ('pModelDataBuffer', POINTER(BYTE)),
    ('byModelingStatus', BYTE),
    ('byLivenessDetectionStatus', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byMask', BYTE),
    ('bySmile', BYTE),
    ('byContrastStatus', BYTE),
    ('byBrokenNetHttp', BYTE),
])

NET_VCA_FACESNAP_MATCH_ALARM = struct_tagNET_VCA_FACESNAP_MATCH_ALARM
LPNET_VCA_FACESNAP_MATCH_ALARM = POINTER(struct_tagNET_VCA_FACESNAP_MATCH_ALARM)
tagNET_VCA_FACESNAP_MATCH_ALARM = struct_tagNET_VCA_FACESNAP_MATCH_ALARM
