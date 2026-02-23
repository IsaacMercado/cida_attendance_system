from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_date import NET_DVR_DATE


class struct_tagNET_DVR_PASSPORT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PASSPORT_INFO, [
    ('dwSize', DWORD),
    ('byOCR', BYTE),
    ('byRes1', BYTE * 3),
    ('byType', BYTE * 4),
    ('byCountryIssue', BYTE * 128),
    ('byName', BYTE * 64),
    ('byPassportNo', BYTE * 16),
    ('byNationality', BYTE * 16),
    ('struBirth', NET_DVR_DATE),
    ('struExpireDate', NET_DVR_DATE),
    ('bySex', BYTE),
    ('byRes2', BYTE * 35),
    ('byLocalName', BYTE * 128),
    ('byNumber', BYTE * 128),
    ('byPlaceOfBirth', BYTE * 128),
    ('byAddr', BYTE * 128),
    ('byPhone', BYTE * 128),
    ('byJob', BYTE * 128),
    ('byTitle', BYTE * 128),
    ('byResume', BYTE * 128),
    ('byOtherNumber', BYTE * 128),
    ('byMonitoring', BYTE * 1024),
    ('byRes', BYTE * 128),
])

NET_DVR_PASSPORT_INFO = struct_tagNET_DVR_PASSPORT_INFO
LPNET_DVR_PASSPORT_INFO = POINTER(struct_tagNET_DVR_PASSPORT_INFO)
tagNET_DVR_PASSPORT_INFO = struct_tagNET_DVR_PASSPORT_INFO
