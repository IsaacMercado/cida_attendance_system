from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_humanattribute_cond import NET_VCA_HUMANATTRIBUTE_COND
from .net_vca_search_database_param import NET_VCA_SEARCH_DATABASE_PARAM


class struct_tagNET_VCA_SEARCH_FACEDB_COND(Structure):
    pass

_S(struct_tagNET_VCA_SEARCH_FACEDB_COND, [
    ('dwDataBaseID', DWORD),
    ('struAttribute', NET_VCA_HUMANATTRIBUTE_COND),
    ('struSearchParam', NET_VCA_SEARCH_DATABASE_PARAM),
    ('dwMaxSearchNum', DWORD),
    ('wThreshold', WORD),
    ('byRes', BYTE * 78),
])

NET_VCA_SEARCH_FACEDB_COND = struct_tagNET_VCA_SEARCH_FACEDB_COND
LPNET_VCA_SEARCH_FACEDB_COND = POINTER(struct_tagNET_VCA_SEARCH_FACEDB_COND)
tagNET_VCA_SEARCH_FACEDB_COND = struct_tagNET_VCA_SEARCH_FACEDB_COND
