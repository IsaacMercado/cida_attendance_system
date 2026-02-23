from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_event_linkage_info import NET_DVR_EVENT_LINKAGE_INFO


class union_tagNET_DVR_EVETN_CARD_LINKAGE_UNION(Union):
    pass

_S(union_tagNET_DVR_EVETN_CARD_LINKAGE_UNION, [
    ('byCardNo', BYTE * 32),
    ('struEventLinkage', NET_DVR_EVENT_LINKAGE_INFO),
    ('byMACAddr', BYTE * 6),
    ('byEmployeeNo', BYTE * 32),
])

NET_DVR_EVETN_CARD_LINKAGE_UNION = union_tagNET_DVR_EVETN_CARD_LINKAGE_UNION
LPNET_DVR_EVETN_CARD_LINKAGE_UNION = POINTER(union_tagNET_DVR_EVETN_CARD_LINKAGE_UNION)
tagNET_DVR_EVETN_CARD_LINKAGE_UNION = union_tagNET_DVR_EVETN_CARD_LINKAGE_UNION
