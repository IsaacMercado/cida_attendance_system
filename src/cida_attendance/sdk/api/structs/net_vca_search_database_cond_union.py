from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_advance_search_database_cond import NET_VCA_ADVANCE_SEARCH_DATABASE_COND
from .net_vca_register_pic import NET_VCA_REGISTER_PIC


class union_tagNET_VCA_SEARCH_DATABASE_COND_UNION(Union):
    pass

_S(union_tagNET_VCA_SEARCH_DATABASE_COND_UNION, [
    ('uLen', DWORD * 25),
    ('struNormalFind', NET_VCA_REGISTER_PIC),
    ('struAdvanceFind', NET_VCA_ADVANCE_SEARCH_DATABASE_COND),
])

NET_VCA_SEARCH_DATABASE_COND_UNION = union_tagNET_VCA_SEARCH_DATABASE_COND_UNION
LPNET_VCA_SEARCH_DATABASE_COND_UNION = POINTER(union_tagNET_VCA_SEARCH_DATABASE_COND_UNION)
tagNET_VCA_SEARCH_DATABASE_COND_UNION = union_tagNET_VCA_SEARCH_DATABASE_COND_UNION
