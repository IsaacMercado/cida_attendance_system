from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_vca_search_database_param import NET_VCA_SEARCH_DATABASE_PARAM


class struct_tagNET_VCA_SEARCH_SNAPDB_COND(Structure):
    pass

_S(struct_tagNET_VCA_SEARCH_SNAPDB_COND, [
    ('dwChannel', DWORD),
    ('dwDataBaseID', DWORD),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('bySex', BYTE),
    ('byRes1', BYTE * 3),
    ('byStartBirthDate', BYTE * 10),
    ('byEndBirthDate', BYTE * 10),
    ('byAttribute1', BYTE * 32),
    ('byAttribute2', BYTE * 32),
    ('struSearchParam', NET_VCA_SEARCH_DATABASE_PARAM),
    ('dwMaxSearchNum', DWORD),
    ('wThreshold', WORD),
    ('byRes', BYTE * 78),
])

NET_VCA_SEARCH_SNAPDB_COND = struct_tagNET_VCA_SEARCH_SNAPDB_COND
LPNET_VCA_SEARCH_SNAPDB_COND = POINTER(struct_tagNET_VCA_SEARCH_SNAPDB_COND)
tagNET_VCA_SEARCH_SNAPDB_COND = struct_tagNET_VCA_SEARCH_SNAPDB_COND
