from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_search_database_cond_union import NET_VCA_SEARCH_DATABASE_COND_UNION


class struct_tagNET_VCA_SEARCH_DATABASE_PARAM(Structure):
    pass

_S(struct_tagNET_VCA_SEARCH_DATABASE_PARAM, [
    ('dwSearchType', DWORD),
    ('uSearchCond', NET_VCA_SEARCH_DATABASE_COND_UNION),
    ('byRes', BYTE * 16),
])

NET_VCA_SEARCH_DATABASE_PARAM = struct_tagNET_VCA_SEARCH_DATABASE_PARAM
LPNET_VCA_SEARCH_DATABASE_PARAM = POINTER(struct_tagNET_VCA_SEARCH_DATABASE_PARAM)
tagNET_VCA_SEARCH_DATABASE_PARAM = struct_tagNET_VCA_SEARCH_DATABASE_PARAM
