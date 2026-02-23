from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_VCA_SEARCH_SNAPRECORD_RESULT(Structure):
    pass

_S(struct_tagNET_VCA_SEARCH_SNAPRECORD_RESULT, [
    ('dwSize', DWORD),
    ('dwDataBaseID', DWORD),
    ('dwRecordID', DWORD),
    ('struSnapTime', NET_DVR_TIME),
    ('bySex', BYTE),
    ('byRes1', BYTE * 3),
    ('byStartBirthDate', BYTE * 10),
    ('byEndBirthDate', BYTE * 10),
    ('byAttribute1', BYTE * 32),
    ('byAttribute2', BYTE * 32),
    ('fSimilarity', c_float),
    ('dwFacePicID', DWORD),
    ('dwFacePicLen', DWORD),
    ('byRes', BYTE * 80),
    ('pFacePic', POINTER(BYTE)),
])

NET_VCA_SEARCH_SNAPRECORD_RESULT = struct_tagNET_VCA_SEARCH_SNAPRECORD_RESULT
LPNET_VCA_SEARCH_SNAPRECORD_RESULT = POINTER(struct_tagNET_VCA_SEARCH_SNAPRECORD_RESULT)
tagNET_VCA_SEARCH_SNAPRECORD_RESULT = struct_tagNET_VCA_SEARCH_SNAPRECORD_RESULT
